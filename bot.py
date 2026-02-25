import time
import pandas as pd
import talib 
from binance.client import Client
from binance.enums import*

# Ne divulgue jamais tes APIs si tu veux pas te faire sucrer ton argent 
API_KEY = "mettre_clé_API ici"
API_SECRET = "mettre_clé_API_Secret ici"

client = Client(API_KEY,API_SECRET)  # Connexion a Binance grâce à mon APIs

SYMBOL = "BTCUSDC"  # Symbole à trader
QUANTITY = 0.001  # Quantité à trader (ici 0.001 BTC)
TIMEFRAME = Client.KLINE_INTERVAL_1MINUTE  # Je choisis l'intervalle de temps, 1 minutes pour du sclaping
LIMIT = 100  # Nombres de bougies récupérer pour l'analyse technique
SLEEP_TIME = 65  # Définie le temps de pose entre chaque analyse (en sec)


#  La fonction suivante télécharge les bougies, les "nettoie" et les convertit en DataFrame prêt à être analyser
def get_market_data(symbol, timeframe, limit):
    klines = client.get_klines(symbol = symbol, interval = timeframe, limit = int(limit))  # Récupère bougies depuis API binance
    df = pd.DataFrame(klines, columns=["timestamps", "open", "high", "low", "close", "volume", "_", "_", "_", "_", "_", "_"])  # Converti en DataFrame Pandas
    df["timestamps"] = pd.to_datetime(df["timestamps"], unit = "ms")  # Convertir l'unité timestamps en date lisible
    df["close"] = df["close"].astype(float)  # Binance renvoi prix en 'str', je converti en 'float' pour avoir des chiffres et manipuler
    return df


#  La fonction suivante ajoute les indicateurs à notre DataFrame, pour ce bot MM20 + RSI
def add_indicators(df):
    df["RSI"] = talib.RSI(df["close"], timeperiod=14) # Ajout du RSI depuis Ta-lib
    df["MA20"] = talib.SMA(df["close"], timeperiod=20) # Ajout de MA 20 depuis Ta-lib
    return df


#  Cette fonction sera notre celle qui nous donnera nos signaux sous conditions
def get_trading_signal(df):
    last_row = df.iloc[-1]
    if pd.isna(last_row["RSI"]) or pd.isna(last_row["MA20"]):
        return "Ne rien faire"
    if last_row["RSI"] < 30 and last_row["close"] < last_row["MA20"]:
        return "Acheter"
    elif last_row["RSI"] > 70 and last_row["close"] > last_row["MA20"]:
        return "Vendre"
    return "Ne rien faire"


# Fonction qui permet d'acheter du BTC
def place_buy_order(symbol, quantity):
    try:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print(f"✅ Achat effectué ! Détails : {order}")
    except Exception as e:
        print(f"❌ Erreur à l'achat : {e}")


# Fonction qui permet de vendre
def place_sell_order(symbol, quantity):
    try:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print(f"✅ Vente effectuée ! Détails : {order}")
    except Exception as e:
        print(f"❌ Erreur à la vente : {e}")


in_position = False # Indique si deja en trade, si oui pas d'achat (1 position a la fois)
last_signal = "Ne rien faire"  # Sert a éviter les ordres répétés

print("🤖 Bot de trading démarré...")

# Boucle infinie → le bot tourne en continu
while True:
    try:

        df = get_market_data(SYMBOL, TIMEFRAME, LIMIT) # Récup bougie depuis binance
        df = add_indicators(df) # ajoute les indicateurs
        signal = get_trading_signal(df) # Vérifie signal de trading
        price = df.iloc[-1]["close"]   # affichage dernier prix
        rsi = df.iloc[-1]["RSI"]       # affichage dernier RSI
        # Maintenant on affiche l'état actuel du marché
        now = df.iloc[-1]["timestamps"].strftime("%d/%m/%Y %H:%M:%S")
        print("\n" + "="*55)
        print(f"🕒 Prix actuel ({now}) du BTC est : {price:.2f} Usdc")
        print(f"📊 Le RSI est à : {rsi:.2f} points")
        print(f"📌 Consigne : {signal}")
        print(f"💼 En position : {in_position}")
        print("="*55)
        print(f"⏳ Prochaine actualisation dans 60 secondes, veuillez patienter...\n")

        # Si signal d'achat ET qu'on ne possède rien
        # Trade uniquement si le signal change du précédent

        if signal != last_signal:

            if signal == "Acheter" and not in_position:
                place_buy_order(SYMBOL, QUANTITY)
                in_position = True   # on marque qu'on est maintenant en position

            # Si signal de vente ET qu'on possède déjà du BTC
            # on ferme la position
            elif signal == "Vendre" and in_position:
                place_sell_order(SYMBOL, QUANTITY)
                in_position = False  # on repasse sans position

        # Mise à jour de last_signal pour le prochain tour
        last_signal = signal 

        
        # Maintenant, il attend 65s quoi qu'il arrive.
        print(f"⏳ Prochaine actualisation dans {SLEEP_TIME} secondes...")
        time.sleep(SLEEP_TIME)

    # Gestion d'erreur → le bot ne s'arrête pas si problème réseau/API
    except Exception as e:
        print(f"⚠️ Erreur inattendue : {e}")
        time.sleep(10)
