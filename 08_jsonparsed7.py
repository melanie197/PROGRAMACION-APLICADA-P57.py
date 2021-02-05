# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:44:33 2021

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
        print("Kilom:           "+str((json_data["route"]["distance"])*1.61))
        print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"]))
        print("===============================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"])+ "("+str("{:.2}".format((each["distance"])*1.61) + "km)"))
            print("===============================\n")
    elif json_status== 402:
        print("**************************")
        print("For Status Code:  " +str(json_status)+ ", Refer to: ")
        
        print("**************************\n")
        print("=====================")
    else:
        print("*****************************")
        print("For Status Code: " + str(json_status)+", Refer to: ")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("*********************************")
        