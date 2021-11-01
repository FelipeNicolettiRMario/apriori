import pandas as pd
import matplotlib.pyplot as plt

def bar_chart_by_product_selled(dataframe: pd.DataFrame) -> None:

    grouped_by_item = dataframe.groupby('Item',as_index=False)['Transaction'].count()

    bar_chart_data = list(grouped_by_item['Transaction'])
    bar_chart_columns = list(grouped_by_item['Item'])

    plt.bar(bar_chart_columns,bar_chart_data)
    plt.title('Product by transaction count')
    plt.show()


def _bar_chart_with_filter(dataframe: pd.DataFrame,filter: str, label:str = '') -> None:
    filtered_frame = dataframe.query(filter)
    grouped_by_item = filtered_frame.groupby('Item',as_index=False)['Transaction'].count()

    bar_chart_data = list(grouped_by_item['Transaction'])
    bar_chart_columns = list(grouped_by_item['Item'])

    plt.bar(bar_chart_columns,bar_chart_data)
    plt.title(f'Product by transaction {label}')
    plt.show()

def bar_chart_by_product_selled_in_morning(dataframe: pd.DataFrame) -> None:
    _bar_chart_with_filter(dataframe,'period_day == "morning"','in morning')

def bar_chart_by_product_selled_in_afternoon(dataframe: pd.DataFrame) -> None:
    _bar_chart_with_filter(dataframe,'period_day == "afternoon"','in afternoon')

def bar_chart_by_product_selled_in_evening(dataframe: pd.DataFrame) -> None:
    _bar_chart_with_filter(dataframe,'period_day == "evening"','in evening')
