from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

import yfinance as yf
yf.pdr_override()

start= dt.datetime(2006,1,1)
end = dt.datetime(2016,1,1)

import cgi
form = cgi.FieldStorage()
searchterm = form.getvalue('ticks')

print(searchterm)

tickers = ['BAC','C','GS','JPM','MS','WF']

d = {}
dataFrames = []
for tick in tickers:
    d[tick] = data.get_data_yahoo(tick, start, end)
    dataFrames.append(d[tick])

bank_stocks = pd.concat(dataFrames,axis=1,keys=tickers)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

import plotly as py
import plotly.graph_objs as go
import cufflinks as cf
cf.go_offline()

fig = bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()
