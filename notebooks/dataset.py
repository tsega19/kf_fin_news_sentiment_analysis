# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
print(os.path.exists("data/raw_analyst_ratings.csv"))

def load_and_prepare_data(data_path):
    """
    Load the dataset and prepare it by converting date columns and extracting year, month, and day.

    Parameters:
        data_path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    data = pd.read_csv(data_path)
    data = convert_date(data)   
    return data    
def convert_date(data):
    """
    Convert 'date' column to datetime and extract year, month, and day.

    Parameters:
        data (pd.DataFrame): Input DataFrame containing a 'date' column.

    Returns:
        pd.DataFrame: Updated DataFrame with 'year', 'month', and 'day' columns.
    """
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    return data

# Call the function and describe the data
# data = load_and_prepare_data("data/raw_analyst_ratings.csv")
# print(data.describe())

def data_summary(df):
    # This function takes a DataFrame as input and returns a summary of its contents.
    # It includes the first few rows of the DataFrame (using head()), 
    # general information about the DataFrame (using info()), 
    # descriptive statistics for numerical columns (using describe()), 
    # and the shape of the DataFrame (number of rows and columns).
    info = df.head(), df.info(), df.describe(), df.shape
    return info

def calculate_headline_statistics(data):
    """
    Calculate descriptive statistics for headline lengths.

    Parameters:
        data (pd.DataFrame): Input DataFrame with a 'headline' column.

    Returns:
        pd.Series: Descriptive statistics of headline lengths.
    """
    headline_lengths = data['headline'].str.len()
    return headline_lengths.describe()

def count_articles_per_publisher(data):
    """
    Count the number of articles per publisher.

    Parameters:
        data (pd.DataFrame): Input DataFrame with a 'publisher' column.

    Returns:
        pd.Series: Counts of articles per publisher.
    """
    return data['publisher'].value_counts()

def plot_publication_trends(data):
    """
    Plot the trends of article publications over time.

    Parameters:
        data (pd.DataFrame): Input DataFrame with a 'date' column.

    Returns:
        None
    """
    publication_trends = data['date'].dt.date.value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.plot(publication_trends.index, publication_trends.values, label="Articles Published")
    plt.title("Publication Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.legend()
    plt.show()

def save_processed_data(data, output_path):
    """
    Save the processed DataFrame to a CSV file.

    Parameters:
        data (pd.DataFrame): DataFrame to save.
        output_path (str): Path to save the CSV file.

    Returns:
        None
    """
    output_path = 'processed_data.csv'
    data.to_csv(output_path, index=False)