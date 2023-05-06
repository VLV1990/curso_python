material_prenda = input("Ingresa el material de la prenda: puede ser'algodon','poliester' o 'nilon': ")
capacidad_lavadora = float(input("Ingresa la capacidad de la lavadora en kg: puede ser de 20, 10 o 5 : "))

cantidad_agua = 0

if material_prenda == "algodon":
    cantidad_agua = capacidad_lavadora * 12
elif material_prenda == "poliester":
    cantidad_agua = capacidad_lavadora * 6
elif material_prenda == "nilon":
    cantidad_agua = capacidad_lavadora * 3
else:
    print("Ese material no sirve")

if cantidad_agua > 0:
   print("debes agregar: " + str(cantidad_agua) + " litros de agua")
