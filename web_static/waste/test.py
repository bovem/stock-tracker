"""import pandas_datareader.data as web
f = web.DataReader('gs', 'iex-tops')


print(f[:10])"""

from iexfinance import get_market_tops, get_stats_intraday

#print(get_market_tops(output_format="pandas"))
print(get_stats_intraday(output_format="pandas",symbol="AAPL"))
