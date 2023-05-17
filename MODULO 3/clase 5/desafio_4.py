mes = int(input("Ingresa un número del 1 al 12 que representa el mes: "))

if mes < 1 or mes > 12:
    print("El número debe estar entre 1 y 12")
else:   
    if mes <= 3:
        trimestre = 1
    elif mes <= 6:
        trimestre = 2
    elif mes <= 9:
        trimestre = 3
    else:
        trimestre = 4

    print("El mes", mes, "pertenece al trimestre", trimestre)
