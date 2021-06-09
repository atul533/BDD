import json

import jsonpath
import requests
# import bs4


url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
# pretty_res = bs4.BeautifulSoup(response.text, 'lxml')
# print(pretty_res)
json_res = json.loads(response.text)
# print(json_res)

data_size = jsonpath.jsonpath(json_res, 'per_page')[0]

for i in range(data_size):
    print(jsonpath.jsonpath(json_res, 'data['+str(i)+'].email')[0])


