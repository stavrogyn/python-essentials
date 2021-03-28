from bs4 import BeautifulSoup
import requests

resp = requests.get('https://stepik.org/media/attachments/lesson/245130/6.html').content.decode('utf8')
soup = BeautifulSoup(resp, 'html.parser')
table = soup.find('table', attrs = {'class' : 'wikitable sortable'})

cnt = 0
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)