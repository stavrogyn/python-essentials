import xlrd
import requests
import pandas as pd

response = requests.get("https://stepik.org/media/attachments/lesson/245267/salaries.xlsx").content


with open('../data/test_input_2.1.2.xls', 'wb') as data:
    data.write(response)
    table = pd.read_excel('test_input_2.1.2.xls')
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(table)


book = xlrd.open_workbook("../data/test_input_2.1.2.xls")
sheet = book.sheet_by_index(0)
first_item = sheet.row_values(0)[0]
values = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

for element in values:
    print(element)
list_to_compare_salories = list()

for row in values[1:]:
    another_list_of_values = sorted(row[1:])
    print(another_list_of_values)
    list_to_compare_salories.append(int(another_list_of_values[3]))

list_of_medians = sorted(list_to_compare_salories, reverse=True)
print(list_of_medians)
mediana = float(list_of_medians[0])
print(mediana)

for row in values[1:]:
    another_list_of_values = sorted(row[1:])
    if mediana == another_list_of_values[3]:
        print(row[0], end=" ")


space_to_count = dict()

for row in values[1:]:
    for value_in_row in row[1:]:
        if value_in_row not in space_to_count:
            space_to_count[values[0][row.index(value_in_row)]] = value_in_row
        else:
            space_to_count[values[0][row.index(value_in_row)]] += value_in_row


print(sorted(space_to_count.items(), key=lambda item: item[1], reverse=True)[0][0])