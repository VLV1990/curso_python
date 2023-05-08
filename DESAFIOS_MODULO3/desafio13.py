renta_anual = float(input("Ingresa  renta anual? "))

if renta_anual < 10000:
    imposicion = 0.05
elif renta_anual < 20000:
    imposicion = 0.15
elif renta_anual < 35000:
    imposicion = 0.2
elif renta_anual < 60000:
    imposicion = 0.3
else:
    imposicion = 0.45

print(f'la tasa de impuesto es {imposicion * 100} %')