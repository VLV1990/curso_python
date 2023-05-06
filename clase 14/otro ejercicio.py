password = "naruto" 

while True:
    ingreso = input("Ingrese la clave: ") 
    if ingreso == password: 
        print("clave correcta")
        break 
    else:
        print("Clave incorrecta. De nuevo")