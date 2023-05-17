grupo1 = []
grupo2 = []
personas = []

while True:
    nombre = input("Ingrese el nombre de una persona (o escriba 'salir' para terminar): ")
    if nombre == 'salir':
        break
    personas.append(nombre)
    if nombre[0].lower() in 'abcdefghjklm':
        grupo1.append(nombre)
    else:
        grupo2.append(nombre)

print("Grupo 1 (mujeres y hombres con nombres que comienzan con las letras A-M): ", grupo1)
print("Grupo 2 (hombres y mujeres con nombres que comienzan con las letras N-Z): ", grupo2)

