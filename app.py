from flask import Flask, render_template, request
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def get_stock_plot(ticker):
    # Fetch stock data
    stock_data = yf.download(ticker, start="2015-01-01", end="2023-01-01")
    
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
    
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    
    plt.close()
    return f'data:image/png;base64,{plot_url}'

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    if request.method == 'POST':
        ticker = request.form['ticker']
        plot_url = get_stock_plot(ticker)
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
