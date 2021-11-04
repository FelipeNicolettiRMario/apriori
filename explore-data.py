from dotenv import load_dotenv

load_dotenv()

from reports import *
from utils.data_loader import get_data_from_mariadb

from reports.reports import bar_chart_by_product_selled, bar_chart_by_product_selled_in_afternoon, bar_chart_by_product_selled_in_evening, bar_chart_by_product_selled_in_morning
from apriori.apriori import Apriori


data = get_data_from_mariadb('basket')
bar_chart_by_product_selled(data)
bar_chart_by_product_selled_in_morning(data)
bar_chart_by_product_selled_in_afternoon(data)
bar_chart_by_product_selled_in_evening(data)
apriori = Apriori(data)
x = apriori.run_analysis_on_data_set(0.09,0.04)
print(x)