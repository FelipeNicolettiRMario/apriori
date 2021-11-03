import pandas
from sqlalchemy import create_engine
import os

engine = create_engine(os.getenv('BD_URI'))

def get_data_from_mariadb(table_name: str) -> pandas.DataFrame:

    query = f'SELECT * FROM {table_name}'
    data_from_sql = pandas.read_sql(query,con=engine)

    return data_from_sql
