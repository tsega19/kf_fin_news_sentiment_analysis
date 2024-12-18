import pandas as pd
from textblob import TextBlob
import nltk
import matplotlib.pyplot as plt

# Ensure necessary NLTK packages are downloaded
nltk.download('punkt')

def load_data(file_path):
    """Load raw CSV data."""
    return pd.read_csv(file_path)

def add_headline_length(data):
    """Calculate headline length."""
    data['headline_length'] = data['headline'].apply(len)
    return data

def publisher_count(data):
    """Count occurrences of each publisher."""
    return data['publisher'].value_counts()

def parse_dates(data):
    """Parse and normalize dates."""
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    return data

def analyze_sentiment(data):
    """Perform sentiment analysis."""
    data['sentiment'] = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return data

def extract_keywords(data):
    """Extract keywords using NLP."""
    data['keywords'] = data['headline'].apply(lambda x: nltk.word_tokenize(x))
    return data

def set_date_index(data):
    """Set date as the index."""
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    return data

def analyze_time_features(data):
    """Analyze publishing times."""
    data['hour'] = data.index.hour
    data['day_of_week'] = data.index.dayofweek
    return data

def plot_sentiment(data):
    """Plot sentiment over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['sentiment'], label='Sentiment')
    plt.xlabel('Date')
    plt.ylabel('Sentiment')
    plt.title('Sentiment Over Time')
    plt.legend()
    plt.show()

def save_processed_data(data, output_path):
    """Save processed data."""
    data.to_csv(output_path, index=False)
