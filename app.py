import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator, EMAIndicator
from ta.momentum import RSIIndicator

# Set the title of the Streamlit app
st.title("📈 Stock Market Analysis Dashboard")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")

def user_input_features():
    ticker = st.sidebar.text_input("Stock Ticker Symbol (e.g., AAPL, MSFT):", "AAPL")
    start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2022-01-01'))
    end_date = st.sidebar.date_input("End Date", pd.to_datetime('2023-01-01'))
    return ticker, start_date, end_date

ticker_symbol, start_date, end_date = user_input_features()

# Fetch data from Yahoo Finance
@st.cache_data
def get_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    data.reset_index(inplace=True)
    return data

data = get_data(ticker_symbol, start_date, end_date)

# Display the data
st.subheader(f"📊 {ticker_symbol} Stock Data")
st.write(data.tail())

# Plot Closing Price
st.subheader(f"📉 Closing Price of {ticker_symbol}")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(data['Date'], data['Close'], label='Closing Price', color='blue')
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (USD)")
ax1.set_title(f"{ticker_symbol} Closing Price Over Time")
ax1.legend()
st.pyplot(fig1)

# Calculate Moving Averages
st.subheader("📈 Moving Averages")
ma_short = st.sidebar.number_input("Short-term MA window (days):", min_value=1, max_value=100, value=20)
ma_long = st.sidebar.number_input("Long-term MA window (days):", min_value=1, max_value=200, value=50)

# Ensure ma_short < ma_long
if ma_short >= ma_long:
    st.sidebar.error("Short-term MA window must be less than Long-term MA window.")

# Calculate SMA and EMA
sma = SMAIndicator(close=data['Close'], window=ma_short).sma_indicator()
ema = EMAIndicator(close=data['Close'], window=ma_long).ema_indicator()

data['SMA'] = sma
data['EMA'] = ema

# Plot Moving Averages
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(data['Date'], data['Close'], label='Closing Price', color='blue')
ax2.plot(data['Date'], data['SMA'], label=f'SMA {ma_short} days', color='red')
ax2.plot(data['Date'], data['EMA'], label=f'EMA {ma_long} days', color='green')
ax2.set_xlabel("Date")
ax2.set_ylabel("Price (USD)")
ax2.set_title(f"{ticker_symbol} Closing Price with Moving Averages")
ax2.legend()
st.pyplot(fig2)

# Calculate RSI
st.subheader("🔍 Relative Strength Index (RSI)")
rsi_window = st.sidebar.number_input("RSI window (days):", min_value=1, max_value=100, value=14)
rsi = RSIIndicator(close=data['Close'], window=rsi_window).rsi()
data['RSI'] = rsi

# Plot RSI
fig3, ax3 = plt.subplots(figsize=(10, 2))
ax3.plot(data['Date'], data['RSI'], label='RSI', color='purple')
ax3.axhline(70, color='red', linestyle='--')
ax3.axhline(30, color='green', linestyle='--')
ax3.set_xlabel("Date")
ax3.set_ylabel("RSI")
ax3.set_title(f"{ticker_symbol} Relative Strength Index (RSI)")
ax3.legend()
st.pyplot(fig3)

# Display RSI Data
st.write(data[['Date', 'RSI']].tail())

# Interpretation of RSI
st.subheader("📘 RSI Interpretation")
st.write("""
- **RSI > 70:** The stock is overbought (might be overvalued) and could be due for a price correction.
- **RSI < 30:** The stock is oversold (might be undervalued) and could be a good buying opportunity.
""")

