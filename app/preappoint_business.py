# coding:utf-8
import requests
import json

nginx_server_url = 'http://192.168.61.194:30000'
# 步骤：登录成功
# 创建预约号、创建pid、增加推荐人信息（内部包含转端、是否已被激活等逻辑）##########################################
# account.preappoint_bussiness
# passport.accountmappings、passport.passport、passport.passport_contact_channel、passport.passport_login_account
pre_appoint_url = '/yjbapi/account/openstock/preappoint/create'
pre_appoint_data = {
    'mobile_no': '18860971090',
    'captcha_code': '600109',
    'template_no': '4',
    'business_type': 1001,
    'product_id': 1,
    'terminal_type': 2
}
pre_appoint_response = requests.post(nginx_server_url+pre_appoint_url, data=pre_appoint_data)
pre_appoint_resonse_json = json.loads(str(pre_appoint_response.text))
print(pre_appoint_resonse_json)
# print(pre_appoint_resonse_json['code'])
# if pre_appoint_resonse_json['code'] == 2070002:
# print(json.dumps(pre_appoint_resonse_json, sort_keys=True, ensure_ascii=False, indent=4))

# 预约状态查询#########################################
pre_status_query_url = '/yjbapi/account/openstock/preappoint/status/query'
pre_status_query_data = {'preengage_id': 2021051312020099}
pre_status_query_response = requests.get(url=nginx_server_url + pre_status_query_url, params=pre_status_query_data, verify=False)
pre_status_query_response_json = json.loads(pre_status_query_response.text)
# print(json.dumps(pre_status_query_response_json, sort_keys=True, ensure_ascii=False, indent=4))

# 查询预约主表信息
pre_preappoint_query_url = '/yjbapi/account/openstock/preappoint/query'
pre_preappoint_query_data = {
    'preengage_id': 2021051312020099
}
pre_preappoint_query_response = requests.get(url=nginx_server_url + pre_preappoint_query_url, params=pre_preappoint_query_data)
pre_preappoint_query_response_json = json.loads(pre_preappoint_query_response.text)
print(json.dumps(pre_preappoint_query_response_json, sort_keys=True, ensure_ascii=False, indent=4))

# 开户环境检查###################################################
openstock_env_check_url = '/yjbapi/account/openstock/envir/check'
openstock_env_check_data = {
    'mobile_no': '18860971090',
    'business_type': '1000'
}
openstock_env_check_response = requests.get(url=nginx_server_url + openstock_env_check_url, params=openstock_env_check_data)
openstock_env_check_response_json = json.loads(openstock_env_check_response.text)
# print(json.dumps(openstock_env_check_response_json, sort_keys=True, ensure_ascii=False, indent=4))
# 上传档案信息
# account.pre_customer_archive_info、account.pre_customer_archive_info_jour

# else:
#     print(pre_appoint_resonse_json['code'])



