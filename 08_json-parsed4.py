# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:47:46 2021

@author: pc
"""

import  urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
key="VIrvtp6n6tJt14jb5T6GXvZZpalQgR7f"

while True: 
    orig=input('ubicacion inicial: ')
    if orig=="quit" or orig== "q":
       print("saliendo ")
       break        
    dest=input('destino: ')
    if dest== "quit" or dest== "q":
             print("saliendo ")
             break
    url= main_api+ urllib.parse.urlencode({"key": key,"from":orig,"to":dest})
    print("URL: "+(url)) 
    
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    
    if json_status==0:
        print("API Status: " + str(json_status)+ " = A successfull route call.\n")