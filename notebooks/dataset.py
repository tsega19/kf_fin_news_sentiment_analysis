import pandas as pd
import matplotlib.pyplot as plt




def load_data(path):
    df = pd.read_csv(path)
    return df

def data_summary(df):
    info = df.head(), df.info(), df.describe(), df.shape
    return info
def data_visualization(df):
    col = df.columns[object]
    for i in col:
        plt.figure(figsize=(10,5))
        plt.title(i)
        plt.hist(df[i], bins=20)
        plt.show()


