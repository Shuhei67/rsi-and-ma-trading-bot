🤖 Bot de Trading Crypto — RSI + Moyenne Mobile (BTC)

Bot de trading algorithmique en Python utilisant l’API de Binance pour trader automatiquement le BTC avec une stratégie simple de pullback en tendance.
Le bot détecte les baisses violentes (survente RSI) dans une tendance haussière, afin d’acheter à prix réduit puis revendre plus haut.

📈 Stratégie

Conditions d’achat
Le bot achète du BTC lorsque :
Le prix est sous la moyenne mobile 20 périodes (MA20)
ET le RSI < 30 (zone de survente)
👉 On profite donc d’un retracement rapide pour entrer à meilleur prix.

Conditions de vente
Le bot vend lorsque :
Le prix est au-dessus de la MA20
ET le RSI > 70 (zone de surachat)

⚠️ Important

Cette stratégie fonctionne uniquement en marché directionnel / tendance.
Exemple d’utilisation recommandée :
Bot en 1 minute
Vérification d’une tendance haussière sur 15 minutes
❌ Éviter les marchés en range (latéral) → faux signaux fréquents.

🧠 Logique du bot

Télécharge les bougies via l’API Binance
Calcule :
RSI (14)
Moyenne Mobile (20)
Génère un signal :
Acheter
Vendre
Ne rien faire
Place un ordre market
Attend 65 secondes
Recommence en boucle

🚨 Sécurité

NE JAMAIS :
partager tes clés
commit tes clés sur GitHub
push ton code avec les clés visibles


🚀 Roadmap

Améliorations prévues :
 Stop loss / Take profit
 Backtesting
 Gestion du risque (% portefeuille)
 Multi-timeframe confirmation
 Logging avancé
 Dashboard
 Support futures / short
 Autres stratégies (breakout, mean reversion, scalping)

 📚 Objectif du projet

Ce projet sert à :
pratiquer le trading algorithmique
apprendre Python appliqué à la finance
expérimenter des stratégies simples
construire des bots plus sophistiqués avec le temps
