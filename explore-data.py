import pandas
from dotenv import load_dotenv
from sqlalchemy import create_engine
from reports import *
import os

from reports.reports import bar_chart_by_product_selled, bar_chart_by_product_selled_in_afternoon, bar_chart_by_product_selled_in_evening, bar_chart_by_product_selled_in_morning

load_dotenv()
engine = create_engine(os.getenv('BD_URI'))

def get_data_from_mariadb(table_name: str) -> pandas.DataFrame:

    query = f'SELECT * FROM {table_name}'
    data_from_sql = pandas.read_sql(query,con=engine)

    return data_from_sql

data = get_data_from_mariadb('basket')
bar_chart_by_product_selled(data)
bar_chart_by_product_selled_in_morning(data)
bar_chart_by_product_selled_in_afternoon(data)
bar_chart_by_product_selled_in_evening(data)

