# -*- coding: utf-8 -*-
"""
Created on 9/26/2021

@author: Charles Wang

@expected output:

"春美冰菓室" 的地址為 : 臺北市松山區敦化北路120巷54號
"兄弟大飯店" 的地址為 : 台北市南京東路三段255號
"大潤發中崙店" 的地址為 : 台北市中山區八德路二段306號B2
"台北小巨蛋" 的地址為 : 臺北市松山區南京東路4段2號
"微風南京" 的地址為 : 台北市松山區南京東路三段337號
"星巴克北寧門市" 的地址為 : 台北市松山區南京東路四段56號1樓
"敦化國中" 的地址為 : 臺北市南京東路三段
"林東芳牛肉麵" 的地址為 : 台北市中山區八德路二段322號
"""

import re
import requests
import json
from pprint import pprint
import urllib.parse

_key = ""
search_url = "https://api.bing.microsoft.com/v7.0/search"

headers = {'Ocp-Apim-Subscription-Key': _key}

queries = ["春美冰菓室", "兄弟大飯店", "大潤發中崙店", "台北小巨蛋", "微風南京", "星巴克北寧門市", "敦化國中", "林東芳牛肉麵"]

for q in queries:
    query = q + " 地址"
    params = 'mkt=' + "zh-TW" + '&q=' + urllib.parse.quote(query)

    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        for i in response.json()['webPages']['value']:
            for j in i:
                if j == "snippet":
                    for s in i[j].split("，"):
                        for i in s.split():
                            if "路" in i and "市" in i and i[i.index("路")-1] != "網":
                                address = re.split('：',i)[-1]
                                address = re.split(':',address)[-1]
                                characters_to_remove = ",.。"
                                pattern = "[" + characters_to_remove + "]"
                                address = re.sub(pattern, "", address)
                                print("\n\"" + query.split()[0] + "\" 的" + query.split()[1] + "為 : " + address)
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
            else:
                continue
            break

    except Exception as ex:
        raise ex

