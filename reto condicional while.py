while True:
    x=input("INGRESE UN NUMERO PARA CONTAR:")
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
      print(y)
      y=y+1
      if y>x:
        break