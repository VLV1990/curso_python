words = "Esto es una cadena de texto "

for letter in words:
    print(letter)

#y si queremos imprimir palabra por palabra
word = ''
for letter in words:
        if letter != ' ':
            word += letter
        else:
            print(word)
            word = ''