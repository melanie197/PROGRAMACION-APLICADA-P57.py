aclNum= int(input("cual es el numero del  IPv4 ACL? "))
if aclNum >=1 and aclNum <=99:
    print("ESTE ES UN ESTANDAR IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print("ESTE ES UNA EXTENSION  IPv4 ACL.")
else:
    print("ESTE NO ES UN ESTANDAR  O UNA EXTENSION  IPv4 ACL.")
