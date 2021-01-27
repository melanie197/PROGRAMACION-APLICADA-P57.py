# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:35:18 2021

@author: pc
"""

import  urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig= "Ibarra"
dest="Cuenca"
key="VIrvtp6n6tJt14jb5T6GXvZZpalQgR7f"
url=main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data=requests.get(url).json()
print(json_data)