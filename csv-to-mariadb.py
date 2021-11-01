import pandas
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
engine = create_engine(os.getenv('BD_URI'),echo=False)

def check_if_path_exists(path: str) -> str:

    if os.path.exists(path):
        return path

    else:
        raise FileNotFoundError('Path não encontrado')

def read_file(path: str) -> pandas.DataFrame:

    if check_if_path_exists(path):

        return pandas.read_csv(path)

def explore_dataframe(dataframe: pandas.DataFrame) -> None:

    print(dataframe.describe())
    print('\n\n')
    print(dataframe.head(15))
    print('\n\n')
    print(dataframe.info())

def dataframe_to_maria_db(dataframe: pandas.DataFrame) -> None:

    dataframe.to_sql('basket',if_exists='replace',con=engine,index=False)

file_buffer_df = read_file('./input/basket.csv')
explore_dataframe(file_buffer_df)
dataframe_to_maria_db(file_buffer_df)
