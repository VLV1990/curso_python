requisitos_ingresos = {
    "titulo": "requerido",
    "notas": "requeridos",
    "foto": "opcional"
}

print(requisitos_ingresos)
# acceder a una propiedad
print(f'las notas son de tipo: {requisitos_ingresos ["notas"]}')
# Practica -> Construir un diccionario de datos para guardar las partes de una avion.
# coloque al menos 6 propiedades
# imprima 3 de ellas
# cambie el valor de 2
# al menos debe existir una propiedad booleana, una entera, una flotante
# un arreglo, un diccionario y un string

avion_informacion = {
    "nombre": "boeing",
    "tipo": 747,
    "consumo": 10000,
    "origen": "ee.uu",
    "trayectoria_internacional": True,
    "vuelo": "nocturno",
    "capacidad": "500",
    "año_fabricacion": 2002
}

avion_informacion["tipo"] = "747"
print(f'el tipo de avion es : {avion_informacion["tipo"]}')

avion_informacion["nombre"] = "boeing"
print(f'el nombre del avion es : {avion_informacion["nombre"]}')

avion_informacion["origen"] = "ee.uu"
print(f'el origen del avion es : {avion_informacion["origen"]}')

avion_informacion["tipo"] = "747-X2"
avion_informacion["nombre"] = "mirage"
print(f'el nuevo tipo de avion es: {avion_informacion["tipo"]}')
print(f'el nuevo nombre del avion es: {avion_informacion["nombre"]}')
avion_informacion["trayectoria_internacional"] = False
print(
    f'¿configurado para trayectoria internacional? {avion_informacion["trayectoria_internacional"]}')
# ------------------------------------------------------------------------------------------------------------------

menus = {
    "alta en fibras": ['semillas', 'chia', 'frutos rojos', 'palta', 'banana'],
    "alta en proteinas": ['pollo', 'vacuno', 'pescado', 'queso', 'leche'],
    "alta en carbos": ['azucar', 'vegetales', 'papa', 'arroz', 'harina']
}
peso = input('¿cual es tu peso? ')
if int(peso) >= 60 and int(peso) <= 70:
    print(
        f'debes comer una dieta alta en CARBOS, o sea: {menus["alta en carbos"]}')
elif int(peso) >= 71 and int(peso) <= 80:
    print(f'debes comer una dieta alta en PROTEINAS, o sea: {menus["alta en proteinas"]}')
elif int(peso) >= 81:
    print(f'debes comer una dieta alta en FIBRAS, o sea: {menus["alta en fibras"]}')
else:
    print('lo siento, no tenemos una dieta ajustada a tus caracteristicas de peso')



