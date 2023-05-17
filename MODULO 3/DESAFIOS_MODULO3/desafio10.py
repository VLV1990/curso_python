numerador = int(input('ingrese un numerador: '))
denominador = int(input('ingrese un denominador: '))

if denominador == 0 :
    print(f'no se puede mostrar, indivisible por 0')
else:
    resultado = numerador/denominador
    print(f'{resultado}')