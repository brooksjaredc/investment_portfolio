import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



start = datetime.datetime(2016,1,1)
end = datetime.datetime(2016,3,1)
dates = np.zeros(0)

f = web.DataReader("GOOG", 'google', start, end)

data = pd.DataFrame(f, columns=['Close'])

dates = data.index
datemin = dates.min()
datemax = dates.max()

prices = data['Close'].values
pricemin = prices.min()
pricemax = prices.max()
pricetop = pricemin + (pricemax-pricemin)*1.10


fig, ax = plt.subplots()


ax.plot(dates,prices,color='black',linestyle='solid',linewidth=1.5)
ax.fill_between(data.index, pricemin, prices, facecolor='blue', alpha=0.5)

ax.axis([datemin, datemax, pricemin, pricetop])

fig.autofmt_xdate()
#ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
#plt.gcf()
#plt.draw()

plt.show()
