"""import pandas_datareader.data as web
f = web.DataReader('gs', 'iex-tops')


print(f[:10])"""

from iexfinance import get_market_last, get_stats_intraday,get_iex_listed_symbol_dir, get_available_symbols

#print(get_price(output_format="pandas"))
#print(get_stats_intraday(output_format="pandas",symbol="AAPL"))
print(get_available_symbols(output_format="pandas")[0]['symbol'])
print(get_available_symbols(output_format="pandas")[0]['name'])
