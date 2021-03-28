import requests
import re

site_content = requests.get("http://pastebin.com/raw/7543p0ns").content.decode("utf-8")
set_of_sites = set()
clear_sites = re.findall(r"(<a.+href=[\"\'])(\w+://)?([\w._-]+)([/:]*.*>)", site_content)

for site in clear_sites:
    set_of_sites.add(site[2])
list_of_sites = sorted(list(set_of_sites))
if ".." in list_of_sites:
    list_of_sites.remove("..")
for answer in list_of_sites:
    print(answer)


