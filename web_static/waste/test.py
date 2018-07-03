import pandas_datareader.data as web
f = web.DataReader('gs', 'iex-tops')


print(f[:10])