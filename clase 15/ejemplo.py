frase= input('ingresa una frase')
letra = input('introduce una letra')


frase = "la vida es demasiado corta para aburrirse"
letra = "e"
cnt= 0
for n in frase:
    if n == letra:
        cnt += 1

input( f'la cantidad de veces que "{letra}"  se repite es {cnt}')
        