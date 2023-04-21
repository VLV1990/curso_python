print("====== listas ======")
first_name = "vicente"
last_name = "lepe"
print(first_name + last_name)
print(first_name + " " + last_name)
edad = "32"
titulo = "asesor"
print(edad + " " + titulo)
mensaje1 = "hola " * 3
print(mensaje1)
print(mensaje1)
mensaje33 = "bastian"
print(mensaje33)
mensaje33 += ","
print(mensaje33)
mensaje33 += "lepev"
print(mensaje33)
print(len(mensaje33))
cadena = "esto es una oracion"
posicion = cadena.find("pelo")
print("pelo se encuentra en:",posicion)
posicion = cadena.find("oracion")
print("oracion se encuentra en:",posicion)
texto = "HOLA SOY GERMAN"
texto_en_minusculas = texto.lower()
print(texto_en_minusculas)
cadena = "hola, soy mundo"
nueva_cadena = cadena.replace("mundo", "harry")
print(nueva_cadena)
variable1 = "hola, holas"
variable2 = variable1.replace("holas","que talca")
print(variable2)
print("====== listas ======")
empty_list = []
print(empty_list)
fullfiled_List = [1,3,500,1.4,[2,"a"],{"name":"richar"},(1,3,5)]
print(fullfiled_List)
second_list = list()
print(second_list)
print(list("concurso de matematicas"))
range_one = range(590)
print(list(range_one))
numeros = [1,4,6]
print(numeros)
numeros.append(10)
print(numeros)
print(numeros[2])
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)
lista = ["perro", "gato", "conejo"]

for indice, valor in enumerate(lista):
    print("El elemento en el índice", indice, "es", valor)
#eliminar cosas en python 

animales = ["perro", "gato", "conejo"]
animales.remove("gato")
print(animales)
#modificar elementos de una lista
lista = [1, 2, 3, 4, 5]
lista[2] = 6
print(lista) 
#iterar lista 
listadeanimales = [1, 2, 3, 4, 5]

for elemento in listadeanimales:
    print(elemento)
listaiterada = ["perro", "gato", "conejo","cerdo","canario"]

for indice, valor in enumerate(listaiterada):
    print("El elemento en el índice", indice, "es", valor)
#otra forma de metodo for
print(listaiterada)
listaiterada = ["perro", "gato", "conejo","cerdo","canario"]
for y in lista:
    print(y)
#modificar elementos de una lista
lista = [1, 2, 3, 4, 5, 7,]
lista[4] = 77
print(lista)
listaAnime = ["dbz","caballerosDelZodiaco","Sailor moon"]
listaAnime[2] = "naruto"
print(listaAnime)