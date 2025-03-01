import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data
ticker = "AAPL"  # Apple Inc. as an example
stock_data = yf.download(ticker, start="2022-01-01", end="2023-01-01")

# Calculate moving averages
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

# Plot closing price and moving averages
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['MA50'], label='50-Day MA')
plt.plot(stock_data['MA200'], label='200-Day MA')
plt.title(f'{ticker} Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot volume
plt.figure(figsize=(14, 7))
plt.bar(stock_data.index, stock_data['Volume'], width=1.0)
plt.title(f'{ticker} Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()
