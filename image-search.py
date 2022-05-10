# -*- coding: utf-8 -*-
"""
Created on 5/10/2022

@author: Charles Wang
"""

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from pprint import pprint

_key = ""
search_url = "https://api.bing.microsoft.com/v7.0/search"
search_term = "哈士奇"

headers = {"Ocp-Apim-Subscription-Key" : _key}
params  = {"q": search_term, "customconfig": '0', "count": "16", 
"offset": "0", "mkt":" zh-TW", "safeSearch":"Moderate" }

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()

search_results = response.json()
pprint(search_results)

thumbnail_urls = [img["thumbnailUrl"] for img in search_results["images"]["value"]]
f,axes = plt.subplots(4, 4)


for i in range(4):
    for j in range(4):
        image_data = requests.get(thumbnail_urls[i*4+j])
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))
        axes[i][j].imshow(image)
        axes[i][j].axis("off")
plt.show()
