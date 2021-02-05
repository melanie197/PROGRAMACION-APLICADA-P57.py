# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:07:45 2021

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
        print("Directions from:  " +(orig)+ " to " +(dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"]))
        print("===============================")