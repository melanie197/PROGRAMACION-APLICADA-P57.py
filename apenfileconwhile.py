# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:06:54 2021

@author: pc
"""

file=open("devices.txt","a")

while True:
    newItem=input("Ingrese nuevo dispositivo: ")
    if newItem=="exit":
      print("LISTPO" +"\n")
      break
    else:
       file.write(newItem+"\n")
file.close()
       