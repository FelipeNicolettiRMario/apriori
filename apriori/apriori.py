import pandas as pd

class Apriori:

    def __init__(self,data) -> None:
        self.data : pd.DataFrame = data
        self.transactions = self._store_transactions()
        self.items = self._store_items()

    def _store_transactions(self) -> pd.DataFrame:
        transaction_limited = self._keep_only_two_itens_transaction()
        transactions = self._merge_transactions(transaction_limited)

        return transactions

    def _keep_only_two_itens_transaction(self):

        counting_transaction_frequence = self.data['Transaction'].value_counts()
        filtered_data = self.data[self.data['Transaction'].isin(counting_transaction_frequence.index[counting_transaction_frequence == 2])]
        return filtered_data

    def _merge_transactions(self,data) -> None:
        keep_first = data.drop_duplicates('Transaction',keep = 'first')
        keep_last = data.drop_duplicates('Transaction',keep='last')

        single_transactions_data = pd.merge(keep_first,keep_last,on='Transaction')

        return single_transactions_data

    def _store_items(self) -> list:

        items = self.data['Item']
        return list(items)

    def _support(self, x: str, y: str) -> float:

        items_popularity_initial_order = len(self.transactions.query(f'(Item_x == "{x}" and Item_y == "{y}")'))
        items_popularity_alternative_order = len(self.transactions.query(f'(Item_x == "{y}" and Item_y == "{x}")'))
        support = (items_popularity_alternative_order + items_popularity_initial_order )/ len(set(self.items))
        
        return support

    def _confidence(self, x: str, y: str) -> float:

        items_popularity_initial_order = len(self.transactions.query(f'Item_x == "{x}" and Item_y == "{y}"'))
        confidence = (items_popularity_initial_order) / self.items.count(x)

        return confidence

    def run_analysis_on_data_set(self,min_support = None,min_confidence = None, results_quantity: int = 2) -> list:
        
        rules = list()
        for index, row in self.transactions.iterrows():

            support = self._support(row['Item_x'],row['Item_y'])
            confidence = self._confidence(row['Item_x'],row['Item_y'])
            
            rule = {
                "rule":f'{row["Item_x"]} with {row["Item_y"]}',
                "support":support,
                "confidence":confidence
            }

            if self._control_by_support_and_confidence(rule,min_support, min_confidence):
                rules.append(rule)

        return self._order_by_confidence(rules,results_quantity)

        

    def _order_by_confidence(self,rules: list, max_results:int) -> list:

        result_with_no_duplicates = list()
        result_sort = sorted(rules,key=lambda x:(x['confidence'],x['support']))
        [result_with_no_duplicates.append(x) for x in result_sort if x not in result_with_no_duplicates]

        return result_with_no_duplicates[- max_results:]

    def _control_by_support_and_confidence(self,rule: dict, min_support: float, min_confidence: float) -> bool:

        if min_support and min_confidence:

            if rule.get('support') >= min_support and rule.get('confidence') >= min_confidence:

                return True
            
            return False

        return True
