from etl.extract import extract_from_csv
from etl.transform import transform
from etl.load import load_to_postgres

def run_etl():
    #Step 1:Extract
    df_raw = extract_from_csv("Data/orders.csv")
    print("Data Extracted")
    print(df_raw)

    df_clean = transform(df_raw)
    print("Data Transformed")
    print(df_clean)

    load_to_postgres(df_clean)
    print("Data loaded")



if __name__ == "__main__":
    run_etl()