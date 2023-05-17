edad_minima = 16
ingresos_tope = [1000]

anios = int(input("¿Cuántos años tienes? "))
ingreso = int(input("¿ingreso mensual? "))

if anios > edad_minima and ingreso >= ingresos_tope:
    print("debes pagar impuestos")
else:
    print("No cumples los requisitos")
      


