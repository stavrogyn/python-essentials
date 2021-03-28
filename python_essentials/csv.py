import pandas as pd

with open('../data/test_input_3.5.2.csv', 'r') as data:
    data_table = pd.read_csv(data)
    data_table = data_table.sort_values('Primary Type')
    print(data_table)
    frequently = data_table['Primary Type'].value_counts()
    print(frequently)