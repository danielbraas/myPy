# This was taken from: https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020

import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf[['Open','High','Low']])
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
st.checkbox('Something?')
st.dataframe(tickerDf)
import pandas_bokeh
pandas_bokeh.output_notebook() # Setting output to notebook

#tickerDf.plot_bokeh(
#    kind='line',
#    x='Date',
#    y=['Open', 'High', 'Low', 'Close'],
#    xlabel='Date',
#    ylabel='Value ($)',
#    title='Google stock value by date'
#)