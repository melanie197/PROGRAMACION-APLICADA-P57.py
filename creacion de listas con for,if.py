lista1=["R1","R2","R3","S1","S2","S3"]
#crear 2 listas en blanco y llenarlas 

switches=[]
for i in lista1:
    if "S"in i:
        switches.append(i)
        print(i)
print("\n")      
routers=[]
for i in lista1:
    if "R"in i:
        routers.append(i)
        print(i)
        
               
