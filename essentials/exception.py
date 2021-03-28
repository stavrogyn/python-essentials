import requests
import re


def causes_searcher(site_content, final_site):
    sites_from_first_site = re.findall(r'http\S+html', site_content)
    if len(sites_from_first_site) >= 1:
        for site in sites_from_first_site:
            try:
                addition_request_text = requests.get(site).text
                additional_sites = re.findall(r'http\S+html', addition_request_text)
                for addition_site in additional_sites:
                    if addition_site == final_site:
                        return True
            except BaseException:
                return False
    return False

try:
    first_site_content = requests.get(input()).text
    second_site = input()
    decision = causes_searcher(first_site_content, second_site)
    if decision:
        print("Yes")
    else:
        print("No")
except BaseException:
    print('No')
