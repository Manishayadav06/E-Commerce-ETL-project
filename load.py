import sqlalchemy

def load_to_postgres(df):
    engine = sqlalchemy.create_engine('postgresql://postgres:tiger@localhost:5432/ecommerce')

    df.to_sql('orders', engine, if_exists='replace',index=False) 