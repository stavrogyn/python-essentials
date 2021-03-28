import requests
import json
import pandas as pd
import pprint

client_id = '63c565d8ec82de9e5c8c'
client_secret = '8dadc2432108e99e73c5311f1d04ce2c'

token_request = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                              data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

token = json.loads(token_request.text)["token"]
header_of_artist_info_requests = {"X-Xapp-Token" : token}
template_for_requests = "https://api.artsy.net/api/artists/{artist_id}"
dict_with_artist_names = dict()
with open("../data/test_input_2.3.7.txt", "r") as data:
    for artist_id in data:
        print(artist_id)
        artist_id = artist_id.strip()
        artist_info_request = requests.get(template_for_requests.format(artist_id=artist_id), headers=header_of_artist_info_requests)
        artist_info = json.loads(artist_info_request.text)
        dict_with_artist_names[artist_info['sortable_name']] = artist_info["birthday"]
    pprint(dict_with_artist_names)

sorted_dict_with_artists = pd.DataFrame(dict_with_artist_names.items(), columns=['name', 'date']).sort_values(by=['date', 'name'])
print(sorted_dict_with_artists)
sorted_dict_with_artists = sorted_dict_with_artists.drop(['date'], axis='columns')
final_list = sorted_dict_with_artists.values.tolist()
print(final_list)
for name in final_list:
    print(name[0])
