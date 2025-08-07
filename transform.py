import pandas as pd
def transform(df):
    df = df.dropna()
    df['order_date'] = pd.to_datetime(df['order_date'], errors= 'coerce')
    df['revenue'] = df ['amount'] * 1.18 
    df= df.dropna()
    return df