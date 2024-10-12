import csv
import pandas as pd
import numpy as np
from itertools import combinations
df = pd.read_csv('data/train_1.csv', sep=';', encoding='utf-8')
df2=df[['Order ID','Product Name',"order_count"]].copy()
df2 = df2.rename(columns = {"Order ID": "Order_ID","Product Name":"item","order_count":"amount"})
# Find the number of combinations that have bought the most or the least
# I create a list from the listbox that contains all the products in each of the purchases
mylist = df2.pivot(index = 'Order_ID',
          columns = 'item',
          values = 'item').values.tolist()

# The list may contain empty values, so I exclude them from the list
mylist = [[i for i in j if i == i] for j in mylist]

# Use the combinations library to find all pairs of products in each purchase to combine them into a single list
total = []
for i in mylist:
    a = (list(combinations(i,2)))
    for b in a:
        total.append(b)

# To find the number of combinations. Forming, grouping and sorting a data frame from a list
patterns = pd.DataFrame(total,columns = ['item_x', 'item_y'])
patterns = patterns\
    .groupby(['item_x', 'item_y'])\
    .agg({'item_x':'count'})\
    .rename(columns = {'item_x':'count'})\
    .sort_values(['count'], ascending = False)\
    .reset_index()

patterns['combination'] = patterns['item_x'] + " + " + patterns['item_y']
