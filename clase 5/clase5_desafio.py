#1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
#asociada con esa calificación. con al siguiente tabla
  
#   0   - 2     D
#   2.1 - 5     C
#   5.1 - 6     B
#   6.1 - 7     A

def letra_calificacion(promedio):
    if promedio >= 0 and promedio <= 2:
        return "D"
    elif promedio >= 2.1 and promedio <= 5:
        return "C"
    elif promedio >= 5.1 and promedio <= 6:
        return "B"
    elif promedio >= 6.1 and promedio <= 7:
        return "A"
    else:
        return "Calificación inválida"
    
puntaje1 = float(input("Ingrese el primer puntaje: "))
puntaje2 = float(input("Ingrese el segundo puntaje: "))
puntaje3 = float(input("Ingrese el tercer puntaje: "))

promedio = (puntaje1 + puntaje2 + puntaje3) / 3

letra = letra_calificacion(promedio)

print("La calificación promedio es: ", promedio)
print("La letra asociada a la calificación es: ", letra)


# el otro ejemplo
numero = int(input("Ingrese un número para generar la tabla de multiplicación: "))

# Inicializamos el contador
contador = 1

# Utilizamos un bucle while para imprimir la tabla de multiplicación
5




    

    