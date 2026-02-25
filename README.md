# 🤖 Bot de Trading Crypto — RSI + Moyenne Mobile (BTC)<br><br>

Bot de trading algorithmique écrit en Python utilisant l’API Binance pour trader automatiquement le BTC.<br>
La stratégie combine le RSI et une Moyenne Mobile 20 périodes.<br><br>

L’objectif est simple :<br>
Acheter les fortes baisses dans une tendance haussière, puis revendre plus haut.<br><br>

--------------------------------------------------<br><br>

# 📈 Stratégie<br><br>

## ✅ Achat<br>
Le bot achète lorsque :<br>
- Le prix est sous la MA20<br>
- ET le RSI < 30 (zone de survente)<br><br>

👉 On profite d’un retracement violent pour entrer à bas prix.<br><br>

## ✅ Vente<br>
Le bot vend lorsque :<br>
- Le prix est au-dessus de la MA20<br>
- ET le RSI > 70 (zone de surachat)<br><br>

👉 On prend les profits quand le marché est en excès.<br><br>

--------------------------------------------------<br><br>

# ⚠️ Important<br><br>

Cette stratégie fonctionne uniquement dans un marché en tendance.<br><br>

Exemple recommandé :<br>
- Bot en timeframe 1 minute<br>
- Vérifier une tendance haussière sur 15 minutes<br><br>

❌ Éviter les marchés latéraux (range) → faux signaux fréquents.<br><br>

--------------------------------------------------<br><br>

# 🧠 Fonctionnement du bot<br><br>

À chaque boucle :<br>
1. Télécharge les bougies Binance<br>
2. Calcule RSI + MA20<br>
3. Génère un signal (Acheter / Vendre / Ne rien faire)<br>
4. Passe un ordre market si conditions remplies<br>
5. Attend 65 secondes<br>
6. Recommence<br><br>

Une seule position ouverte à la fois pour limiter le risque.<br><br>

--------------------------------------------------<br><br>

# ⚙️ Installation<br><br>

Cloner le projet :<br>
git clone https://github.com/tonpseudo/ton-repo.git<br>
cd ton-repo<br><br>

Installer les dépendances :<br>
pip install pandas ta-lib python-binance<br><br>

TA-Lib peut nécessiter une installation système :<br>
https://ta-lib.org/install/<br><br>

--------------------------------------------------<br><br>

# 🔑 Configuration API<br><br>

Dans le script :<br><br>

API_KEY = "mettre_clé_API ici"<br>
API_SECRET = "mettre_clé_API_Secret ici"<br><br>

--------------------------------------------------<br><br>

# 🚨 Sécurité (TRÈS IMPORTANT)<br><br>

NE JAMAIS :<br>
- partager tes clés API<br>
- commit tes clés sur GitHub<br>
- push tes clés dans ton repo<br><br>

Utilise plutôt :<br>
- variables d’environnement<br>
- fichier .env<br>
- secrets manager<br><br>

Si quelqu’un récupère tes clés → il peut vider ton compte.<br><br>

--------------------------------------------------<br><br>

# ▶️ Lancer le bot<br><br>

python bot.py<br><br>

--------------------------------------------------<br><br>

# 🛠️ Paramètres modifiables<br><br>

SYMBOL = "BTCUSDC"<br>
QUANTITY = 0.001<br>
TIMEFRAME = 1 minute<br>
LIMIT = 100 bougies<br>
SLEEP_TIME = 65 secondes<br><br>

--------------------------------------------------<br><br>

# 📊 Indicateurs utilisés<br><br>

- RSI (14) → surachat / survente<br>
- Moyenne Mobile 20 → direction court terme<br>
- Price Action → confirmation<br><br>

--------------------------------------------------<br><br>

# 🚀 Améliorations prévues<br><br>

- Stop Loss / Take Profit<br>
- Backtesting<br>
- Gestion du risque (%)<br>
- Multi-timeframe<br>
- Dashboard<br>
- Futures / Short<br>
- Nouvelles stratégies<br><br>

--------------------------------------------------<br><br>

# 🎯 Objectif du projet<br><br>

Ce projet me permet de progresser en Python et en trading algorithmique.<br>
Il évoluera avec mon expérience et d’autres bots plus sophistiqués seront ajoutés.<br><br>

--------------------------------------------------<br><br>

# ⚠️ Disclaimer<br><br>

Ce bot est éducatif uniquement.<br>
Le trading comporte des risques.<br>
Tu peux perdre de l’argent.<br><br>

Teste toujours en paper trading ou avec de petites sommes avant.<br>
