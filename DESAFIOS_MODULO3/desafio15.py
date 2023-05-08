puntuacion = float(input("Introduce tu puntuación (0.0/0.4/0.6): "))

if puntuacion == 0.0:
    nivel = "inaceptable"
    dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion
else:
    nivel = "no es válido, puntuación incorrecta"
    dinero = "inválido, puntuación incorrecta"
    print("Puntuación no válida")

print(f'Tu nivel es de: {nivel}')
print(f'Tu bono es de: $ {dinero}')