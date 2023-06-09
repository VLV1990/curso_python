lista_nombres = ['Houdini','Newton','David Blaine','Hawking','Messi','Teller','Einstein','Pele','Juanes']
magos_list = ['Houdini','David Blaine','Teller']

lista_cientificos = [lista_nombres[1], lista_nombres[3], lista_nombres[6]]

lista_otros = [elemento for elemento in lista_nombres
              if elemento not in magos_list and elemento not in lista_cientificos]

def hacer_grandioso():
    for elemento in magos_list:
        print(f'El gran {elemento}')

def imprimir_nombres():
    for elemento in lista_nombres:
        print(f'{elemento}')

print('\n--------------------------------------------------\n')
print('I) lista de magos: ')
hacer_grandioso()
print('\n--------------------------------------------------\n')
print('II) nombres completos: ')
imprimir_nombres()
print('\n--------------------------------------------------\n')
print('III) lista de cientificos: ')
for elemento in lista_cientificos:
    print(elemento)
print('\n--------------------------------------------------\n')
print('IV) lista de otros: ')

for elementos in lista_otros:
    print(elementos)


