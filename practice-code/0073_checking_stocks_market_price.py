# pip install yfinance

import yfinance as yf

stk = input('Enter share name: ')
share = yf.Ticker(stk).info
market_price = share['regularMarketPrice']

print(market_price)