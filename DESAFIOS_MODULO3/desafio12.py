nombre = str(input("Ingresa su nombre: "))
sexo = str(input("Ingresa tu sexo (M/H): "))

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f'Tu nombre es {nombre}, tu sexo es {sexo}, entonces perteneces al grupo {grupo}')