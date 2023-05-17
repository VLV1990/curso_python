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

#lista reverse
lista7 = ['colocolo','udechile','cato',]
lista7.reverse()
print(lista7) 

#extend()
lista8 = [1, 2, 3]
lista9 = [4, 5, 6]
lista8.extend(lista9)
print(lista8) 

lista3 = ['colocolo', 'udechile', 'ucatolica']
lista4 = ['rangers', 'audax', 'huachipato']
lista3.extend(lista4)
print(lista3) 

#append
lista5 = ['colo','uchile','cato']
lista5.append('audax')
print(lista5) 

#nueva tupla
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
nueva_tupla = tupla1 + tupla2
print(nueva_tupla)


#lista vacia
empty_dict_2 = dict()
print(empty_dict_2)
full_dict = dict(
    genero = "M",
    nacionalidad = "E"
)
print(full_dict)

empleado = {
    "name" : "valeria",
    "apellido" : "roso",
    "edad" : 18,
    "rut" : "11.111.111-1"
}

for variablex in empleado.values():
    print(variablex)

empleado2 = {
    "name" : "martin",
    "apellido" : "hernandez",
    "edad" : 88,
    "rut" : "11.111.111-7"
}

for variabley in empleado2.values():
    print(variabley)

print(empleado)
for variable1 in empleado.values():
    print(variable1)



##for variable1 in empleado.value():
   ## print(variable1)

print(empleado2)
for a,b in empleado2.items():
    print(a,b)

print("====== Trabajando con condicionales =====")

edad = 60
if edad > 50:
    print("hola don")
    print("hola dese adentro del if")

print("aca continua el codigo")

# si la temperatura es alta o no
temperatura = 29
if temperatura >= 37:
    print("WARNING!! alerta de temperatura alta")
else:
    print("la temperatura aun es normal")

temperatura = 5
pais = 'chile'
if temperatura <10:
    if pais == "chile":
        print('cccc')
    else:
        print('zzz')
else:
    if pais == 'chile':
        print('111')
    else:
        print('222')

if temperatura <10:
    print("es altamente probable que nieve")
elif temperatura >=10 and temperatura <=20:
    print("es medianamente probable que nieva")
else:
    print("no hay posibilidad de nieve")

#escriba un programa que permita adivinar un personaje de marvel en base a estas 3 preguntas:
#¿ puede volar? 
#¿ Es humano? 
#¿ tiene mascara? 
print("====== ADIVINA EL PERSONAJE/ADIVIAN EL PERSONAJE =====")

puede_volar = False
tiene_mascara = True
es_humano = False

if puede_volar ==True:
    if tiene_mascara == True:
        if es_humano == False:
            print("el vision")

if puede_volar ==True:
    if tiene_mascara == True:
        if es_humano == True:
            print("es iron man")

if puede_volar == True:
    if tiene_mascara == False:
        if es_humano == False:
            print("el superman")

if puede_volar == False:
    if tiene_mascara == False:
        if es_humano == False:
            print("el jack sparrow")

if puede_volar == False:
    if tiene_mascara == True:
        if es_humano == False:
            print("el wakanda")



#trabajando con while
#mientras se cumpla la condicion, ejecuta los siguientes codigo

#   while condicion:
# 

print ("================ trabajando con ciclios: los while")

want_exit = 'n'
while want_exit == 'n':
    print("hola, como estas?")
    want_exit = input("Quieres Salir S/N")
print("fuera del while")

print ("================ trabajando con ciclios: los while")
print ("================ trabajando con ciclios: los while")
print ("================ trabajando con ciclios: los while")
#break, nos permite romper un ciclo 

want_exit = 'n'
num_questions = 0
while want_exit == 'n':
    print("hola como estas?")
    want_exit = input("Quieres salir S/N")
    num_questions += 1
    if num_questions == 4:
        print("Alcansaste el maximo permitido")
        break   
print("se acabo el while")





 
