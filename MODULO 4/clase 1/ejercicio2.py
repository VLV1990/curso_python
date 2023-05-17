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

