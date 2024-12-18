from scripts.stock_analysis import *
from scripts.news_analysis import *
from scripts.correlation import *
from scripts.data_processing import *  # Import the new functions

if __name__ == "__main__":
    # Stock analysis
    filepath = 'AAPL_historical_data.csv'
    data = load_stock_data(filepath)
    data = apply_technical_indicators(data)
    data = calculate_financial_metrics(data)
    plot_stock_prices(data)
    plot_macd(data)
    plot_rsi(data)
    plot_returns(data)
    plot_volatility(data)

    # News and stock data alignment
    news_data_path = 'processed_analyst_ratings.csv'
    stock_data_path = 'AAPL_processed_data.csv'
    output_path = '/data/aligned_news_stock_data.csv'

    # Load datasets
    news_data, stock_data = load_data(news_data_path), load_data(stock_data_path)

    # Add headline length
    news_data = add_headline_length(news_data)

    # Count publishers
    publisher_counts = publisher_count(news_data)

    # Parse and normalize dates
    news_data = parse_dates(news_data)
    stock_data = parse_dates(stock_data)

    # Analyze sentiment
    news_data = analyze_sentiment(news_data)

    # Extract keywords
    news_data = extract_keywords(news_data)

    # Set date as index
    stock_data = set_date_index(stock_data)

    # Analyze time features
    news_data = analyze_time_features(news_data)

    # Align datasets and analyze sentiment
    aligned_data = align_and_analyze_sentiment(news_data, stock_data)

    # Calculate daily returns and correlation
    aligned_data, correlation = calculate_correlation(aligned_data)

    # Visualize the data
    visualize_data(aligned_data)

    # Visualize the correlation of run time and sentiment
    visualize_returns(aligned_data)
    
    # Save the aligned dataset
    save_processed_data(aligned_data, output_path)
