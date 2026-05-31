import pandas as pd
from sqlalchemy import create_engine
import os

def database_creation():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, 'data', 'chinook.db')
    engine = create_engine(f'sqlite:///{DB_PATH}')
    return engine

def sql_practice():
    engine = database_creation()

    # Load data from the CSV file into the database
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, 'data', 'customers.csv')
    df_csv = pd.read_csv(csv_path)

    # Persist the DataFrame to the 'customers' table
    df_csv.to_sql('customers', con=engine, if_exists='replace', index=False)

    df = pd.read_sql_query("SELECT * FROM customers", engine)
    print(df.head())

if __name__ == '__main__':
    sql_practice()
