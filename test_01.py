import ccxt

binance = ccxt.binance()
markets = binance.load_markets()
#print(markets)
#print(type(markets))
#print(markets.keys())
# for market in markets.keys():
#     print(market)
#print(len(markets))

for market in markets.keys():
    if market.endswith("USDT"):    # BTC/USDT
        print(market)