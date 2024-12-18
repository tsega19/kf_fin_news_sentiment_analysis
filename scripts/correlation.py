import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Function to load datasets
def load_datasets(news_data_path, stock_data_path):
    news_data = pd.read_csv(news_data_path)
    stock_data = pd.read_csv(stock_data_path)
    return news_data, stock_data

# Function to parse and normalize dates
def normalize_dates(news_data, stock_data):
    news_data['date'] = pd.to_datetime(news_data['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce').dt.date
    stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.date
    return news_data, stock_data

# Function to align datasets by date and calculate sentiment
def align_and_analyze_sentiment(news_data, stock_data):
    aligned_data = news_data.groupby('date').agg({'headline': ' '.join}).reset_index()
    aligned_data = pd.merge(aligned_data, stock_data, left_on='date', right_on='Date', how='inner')

    # Define sentiment analysis function
    def analyze_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    aligned_data['sentiment'] = aligned_data['headline'].apply(analyze_sentiment)
    return aligned_data

# Function to calculate daily stock returns and correlation
def calculate_correlation(aligned_data):
    aligned_data['daily_return'] = aligned_data['Close'].pct_change()
    correlation = aligned_data[['sentiment', 'daily_return']].corr().iloc[0, 1]
    print(f"Correlation between sentiment and daily returns: {correlation}")
    return aligned_data, correlation

# Function to visualize sentiment
def visualize_data(aligned_data):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(aligned_data['date'], aligned_data['sentiment'], label='Sentiment', color='blue')
    plt.title('Daily Sentiment Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sentiment')
    plt.legend()


# function to Plot daily returns over time
def visualize_returns(aligned_data):
    plt.subplot(2, 1, 2)
    plt.plot(aligned_data['date'], aligned_data['daily_return'], label='Daily Return', color='green')
    plt.title('Daily Stock Returns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function to save the aligned dataset
def save_aligned_data(aligned_data, output_path):
    aligned_data.to_csv(output_path, index=False)
