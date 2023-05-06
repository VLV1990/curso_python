k_inicial = float(input("capital inicial: "))
i_interes = float(input("tasa de interés: "))
z_periodos = int(input("cantidad de años: "))

monto_acumulado_final = k_inicial * (1 + i_interes/100) ** z_periodos

print(f"El monto acumulado final en {z_periodos} años es de: {int(monto_acumulado_final)}")