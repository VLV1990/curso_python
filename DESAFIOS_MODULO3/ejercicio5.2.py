# escribir un programa que pregunte al usuario
# una cantidad a invertir, el interes anual y
# el numero de años, y muestre por pantalla
# el capital obtenido en la inversion

cantidad_a_invertir = int(input('Ingrese la cantidad a invertir: '))
intereses_anual = int(input('Ingrese el interes: '))
cant_anios = int(input('ingrese la cantidad en años: '))

capital_obtenido = cantidad_a_invertir * (1 + (intereses_anual/100))**cant_anios
print(f'el capital obtenido es', "$", round(capital_obtenido, 2), "pesos")