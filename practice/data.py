import requests
import re

site_content = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html').content.decode('utf8')
list_with_constructions = list()
set_values = set()
repetition_counts = dict()
final_value = 0
count_of_oparetions = 0
print(site_content)

preliminary_values = re.findall(r'<\w*?>[\s*]\d+?[\s*]</\w*?>', site_content)

print(len(preliminary_values))

for value in preliminary_values:
    pure_value = re.sub(r'(<\w*?>[\s*])(\d*?)([\s*]</\w*?>)', r'\2', value)
    list_with_constructions.append(pure_value)


print(list_with_constructions)
print(len(list_with_constructions))

for value in list_with_constructions:
    final_value += int(value)
    count_of_oparetions += 1

print(count_of_oparetions)
print(final_value)