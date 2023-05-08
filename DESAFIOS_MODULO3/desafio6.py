peso_payaso = 112
peso_muñeca = 75

num_payasos = int(input('ingresa la cantidad de payasos: '))
num_muñecas = int(input('ingresa la cantidad de muñecas: '))

peso_total = (peso_payaso * num_payasos) + (peso_muñeca * num_muñecas)
print(f'peso total del paquete : {peso_total} g')