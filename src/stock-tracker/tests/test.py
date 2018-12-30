import pandas as pd
import datetime as dt
pd.core.common.is_list_like = pd.api.types.is_list_like #FOR SOME WEIRD IMPORTTING ERROR

import pandas_datareader.data as web
start_date = dt.datetime(2017,1,1)
end_date = dt.datetime.now()
f = pd.DataFrame(web.DataReader('tsla', 'iex', start_date, end_date ))


print(f[:10])

"""

from iexfinance import get_market_last, get_stats_intraday,get_iex_listed_symbol_dir, get_available_symbols

#print(get_price(output_format="pandas"))
#print(get_stats_intraday(output_format="pandas",symbol="AAPL"))
print(get_available_symbols(output_format="pandas")[0]['symbol'])
print(get_available_symbols(output_format="pandas")[0]['name'])
"""