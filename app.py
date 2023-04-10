from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def getValue():
    ticks = request.form['query']
    from pandas_datareader import data, wb
    import pandas as pd
    import numpy as np
    import datetime as dt
    import matplotlib.pyplot as plt

    import yfinance as yf
    yf.pdr_override()

    tickers = list(ticks.split(", "))

    d = {}
    dataFrames = []
    for tick in tickers:
        d[tick] = data.get_data_yahoo(tick)
        dataFrames.append(d[tick])

    bank_stocks = pd.concat(dataFrames,axis=1,keys=tickers)
    bank_stocks.columns.names = ['Bank Ticker','Stock Info']

    bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot(label=tick,figsize=(12,4))
    plt.savefig('stockGraph.png')
    
    return render_template('plot.html', ticks=ticks)

if __name__ == '__main__':
    app.run(debug=True)