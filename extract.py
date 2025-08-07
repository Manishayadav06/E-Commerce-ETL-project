import pandas as pd 
def extract_from_csv(filepath):
    df=pd.read_csv(filepath)
    return df