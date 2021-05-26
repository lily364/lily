# coding:utf-8
import requests

data = {'preengage_id': 2021051312020099}
nginx_server_url = 'http://192.168.61.194:30000'
pre_status_query_url = '/yjbapi/account/openstock/preappoint/status/query'
response = requests.get(url=nginx_server_url+pre_status_query_url, params=data, verify=False)
print(response.text)
print(pre_status_query_url)
print(response)
