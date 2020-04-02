from iexfinance.stocks import get_historical_data, get_historical_intraday

import datetime

start = datetime.datetime(2020, 3, 30)
end = datetime.datetime.today()

#result = get_historical_data("AAPL", start, end, output_format='pandas')
result = get_historical_intraday("AAPL", start, output_format='pandas')
for key,value in result.items():
    print("key:%s value:%s"%(key, value))
