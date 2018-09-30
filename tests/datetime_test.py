"""import datetime as dt
from dateutil import parser
new = parser.parse("2017,1,1","%Y,%m,%d")
print(new)"""

import datetime as dt 
war_start = '2011-01-03'
new = dt.datetime.strptime(war_start, '%Y-%m-%d')
print(new)