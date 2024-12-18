# Import necessary libraries
import pandas as pd
import pandas_ta as ta
import pynance as pn
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load stock data
def load_stock_data(filepath):
    data = pd.read_csv(filepath)
    print(data)
    return data

# Function to apply technical analysis indicators
def apply_technical_indicators(data):
    adx_data = ta.adx(data['High'], data['Low'], data['Close'])
    data = data.join(adx_data)
    data[['stoch_k', 'stoch_d']] = ta.stoch(data['High'], data['Low'], data['Close'])
    data[['macd', 'macd_signal', 'macd_hist']] = ta.macd(data['Close'])
    data['rsi'] = ta.rsi(data['Close'])
    print(data)
    return data

# Function to calculate financial metrics
def calculate_financial_metrics(data):
    if 'Adj Close' not in data.columns:
        if 'Close' in data.columns:
            data = data.rename(columns={'Close': 'Adj Close'})
        else:
            raise KeyError("Neither 'Adj Close' nor 'Close' column found in the DataFrame.")

    data['daily_return'] = pn.tech.ret(data[['Adj Close']])
    data['cumulative_return'] = (1 + data['daily_return']).cumprod()
    data['volatility'] = data['daily_return'].rolling(window=14).std()

    risk_free_rate = 0.02
    annualized_return = data['daily_return'].mean() * 252
    annualized_volatility = data['daily_return'].std() * (252 ** 0.5)
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

    print("\nSharpe Ratio (Annualized):", sharpe_ratio)
    print("\nData with Financial Metrics:")
    print(data.head())
    return data

# Function to plot stock prices and moving averages
def plot_stock_prices(data):
    sns.set_theme(style='darkgrid')
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Close'].rolling(window=20).mean(), label='20-Day SMA', color='orange')
    plt.plot(data['Close'].rolling(window=50).mean(), label='50-Day SMA', color='green')
    plt.title("Stock Price with Moving Averages")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# Function to plot MACD
def plot_macd(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['macd'], label='MACD', color='blue')
    plt.plot(data['macd_signal'], label='Signal Line', color='red')
    plt.bar(data.index, data['macd_hist'], label='MACD Histogram', color='gray', alpha=0.5)
    plt.title("MACD Indicator")
    plt.xlabel("Days")
    plt.ylabel("MACD Value")
    plt.legend()
    plt.show()

# Function to plot RSI
def plot_rsi(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['rsi'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title("Relative Strength Index (RSI)")
    plt.xlabel("Days")
    plt.ylabel("RSI Value")
    plt.legend()
    plt.show()

# Function to plot daily and cumulative returns
def plot_returns(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['cumulative_return'], label='Cumulative Returns', color='blue')
    plt.bar(data.index, data['daily_return'], label='Daily Returns', color='orange', alpha=0.5)
    plt.title("Daily and Cumulative Returns")
    plt.xlabel("Days")
    plt.ylabel("Returns")
    plt.legend()
    plt.show()

# Function to plot volatility
def plot_volatility(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['volatility'], label='Volatility (14-day Rolling)', color='red')
    plt.title("Stock Volatility")
    plt.xlabel("Days")
    plt.ylabel("Volatility")
    plt.legend()
    plt.show()

