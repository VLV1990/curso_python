class Motocicleta:
    is_new = True
    motor = False
    def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas, _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso, _capacidad_tanque):
        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros #litros actuales en la moto
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.capacidad_tanque = _capacidad_tanque  # capacidad maxima
        self.litros_faltantes = self.capacidad_tanque - self.combustible_litros 
        #el constructor solo sirve para inicializar, por lo tanto self.litros_faltantes = self.capacidad_tanque - self.combustible_litros no deberia ir en el constructor. 

    def arrancar(self):
        if not self.motor == False:
            print("El motor ha arrancado")
        else:
            print("El motor ha arrancado")
    def detener(self):
        if self.motor == False:
            print("El motor ya estaba detenido")
        else:
            print("El motor se ha apagado")

    def consultar_precio(self):
        print(f"El precio de la motocicleta {moto1.marca} {moto1.modelo} es de U$ {moto1.precio}")

    def comprobar_combustible(self):
        print(f'La cantidad de combustible en el taque actualmente que tiene la motocicleta {self.marca} {self.modelo} es de {self.combustible_litros} litros.')
        print(f'La capacidad máxima del tanque es de {self.capacidad_tanque} litros.')
        print(f'Faltan {self.litros_faltantes} litros para llenar el tanque.')

    def reporte_combustible(self):
        _marca = input("Ingrese la marca de motoclicleta, puede ser Bajaj o Kawasaki :")
        if _marca == "kawasaki":
            print(f"1. La cap máxima del tanque de combustible de la motocicleta {moto1.marca} es de {moto1.capacidad_tanque} LT")
            print(f"2. La cantidad de combustible en el tanque de la motocicleta {moto1.marca} es de {moto1.combustible_litros} LT.")
            print(f"3. Faltan {moto1.capacidad_tanque - moto1.combustible_litros} LT para llenar el tanque.")

        elif _marca == "bajaj":
            print(f"1. La cap máxima del tanque de combustible de la motocicleta {Moto2.marca} es de {Moto2.capacidad_tanque} LT")
            print(f"2. La cantidad de combustible en el tanque de la motocicleta {Moto2.marca} es de {Moto2.combustible_litros} LT.")
            print(f"3. Faltan {Moto2.capacidad_tanque - Moto2.combustible_litros} LT para llenar el tanque.")
        else:
            print("Marca de motocicleta no válida.")

    def colocar_combustible():
        while True:
            litros_colocar = float(input(' ingrese la cantidad de litros'))


    


#con argumentos posicionales
moto1 = Motocicleta("Negro", "XX22", 15 , 2 , "Kawasaki", "Ninja", "2023/03/10", 200, 120, 17)


#con argumentos claves
Moto2 = Motocicleta(
    _color='naranja',
    _matricula='SS96',
    _combustible_litros=10,
    _numero_ruedas=2,
    _marca='Bajaj',
    _modelo='pulsar',
    _fecha_fabricacion='2023/04/07',
    _velocidad_punta= 180,
    _peso=250,
    _capacidad_tanque= 20)

moto1.arrancar()
moto1.detener()
moto1.precio = 1000
print(f"El precio de  la motocicleta {moto1.marca} {moto1.modelo} es de U$ {moto1.precio}")
moto1.consultar_precio()
moto1.comprobar_combustible()
moto1.reporte_combustible()

