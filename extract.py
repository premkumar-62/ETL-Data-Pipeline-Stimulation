import pandas as pd

def extract_data():
    data = pd.read_csv("data/sales.csv")
    return data