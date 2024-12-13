import pandas as pd
import matplotlib.pyplot as plt




def load_data(path):
    df = pd.read_csv(path)
    return df

def data_summary(df):
    info = df.head(), df.info(), df.describe(), df.shape
    return info
def data_visualization(df):
    plt.hist(df[''], bins=10)
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.title('Sentiment Distribution')
    plt.show()



