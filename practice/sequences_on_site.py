import requests
import re

site_content = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html').content.decode('utf-8')
count_of_c = re.findall(r'[Cc]\+\+', site_content)
count_of_python = re.findall(r'[pP]ython', site_content)

print(count_of_c)
print(count_of_python)

if len(count_of_c) > len(count_of_python):
    print('Count of C++ is', len(count_of_c))
else:
    print('Count of Python is', len(count_of_python))

