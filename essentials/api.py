import requests
import json

with open("../data/test_input_3.6.3.txt", "r") as dataset:
    values_list = list(number.strip() for number in dataset.readlines())
    print(values_list)

template_of_requests = "http://numbersapi.com/{input_value}/math?json=true"

for number in values_list:
    number_request = requests.get(template_of_requests.format(input_value=number))
    fact_about_number = number_request.content.decode("utf-8")
    request_status = number_request.status_code
    print(request_status)
    print(fact_about_number)
    if request_status != 200:
        while request_status != 200:
            print("Retry my previous bad request")
            number_request = requests.get(template_of_requests.format(input_value=number))
            fact_about_number = number_request.content.decode("utf-8")
            request_status = number_request.status_code
    content_from_site = json.loads(fact_about_number)
    interesting_fact = content_from_site["text"]
    interesting_fact_flag = content_from_site["found"]
    print(interesting_fact)
    if interesting_fact_flag:
        print("Interesting")
    else:
        print("Boring")