material_prenda = input("Ingresa el material de la prenda: puede ser'algodon','poliester' o 'nilon': ")
capacidad_lavadora = float(input("Ingresa la capacidad de la lavadora en kg: puede ser de 20, 10 o 5 : "))
marca = input("Ingresa la marca de lavadora: puede ser samsung, LG o daewoo :")
cantidad_agua = 0

if material_prenda == "algodon":
    cantidad_agua = capacidad_lavadora * 12
elif material_prenda == "poliester":
    cantidad_agua = capacidad_lavadora * 6
elif material_prenda == "nilon":
    cantidad_agua = capacidad_lavadora * 3
else:
    print("Ese material no sirve")

if marca == "samsung":
    cantidad_agua = cantidad_agua * 0.2
elif marca == "LG":
    cantidad_agua = cantidad_agua * 0.3
elif marca == "daewoo":
    cantidad_agua = cantidad_agua * 0.5
else:
    print("esa marca no existe")

if cantidad_agua > 0:
   print("debes agregar: " + str(cantidad_agua) + " litros de agua")