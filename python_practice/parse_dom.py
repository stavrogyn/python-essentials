import requests
import re
import numpy as np


list_with_constructions = list()
set_values = set()
repetition_counts = dict()
final_list = list()

site_content = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').content.decode('utf-8')
preliminary_values = re.findall(r'<code>\w*?</code>', site_content)

for value in preliminary_values:
    pure_value = re.sub(r'(<code>)(\w*?)(</code>)', r'\2', value)
    list_with_constructions.append(pure_value)


print(list_with_constructions)

for value in list_with_constructions:
    if value in repetition_counts:
        repetition_counts[value] += 1
    else:
        repetition_counts[value] = 1

sorted_list_with_kays_and_values = (sorted(repetition_counts.items(), key=lambda item: item[1], reverse=True))
print(sorted_list_with_kays_and_values)

biggest_count_of_repetition = sorted_list_with_kays_and_values[0][1]
for value in sorted_list_with_kays_and_values:
    if value[1] == biggest_count_of_repetition:
        final_list.append(value[0])
    else:
        break

print(" ".join(final_list))
