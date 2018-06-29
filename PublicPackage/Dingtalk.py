"""
@file: DingtalkConfig.py
@copyright: laoZ
"""
import requests
import json
from Config.DingtalkConfig import Dingtalk_access_token

'''封装钉钉群发消息'''
def Send_Dingtalk(content):

    url = Dingtalk_access_token

    pagrem = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "isAtAll": True
    }

    headers = {
        'Content-Type': 'application/json'}

    f = requests.post(url, data=json.dumps(pagrem), headers=headers)
    if f.status_code==200:
        return True
    else:
        return False