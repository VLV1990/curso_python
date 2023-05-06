class Motocicleta:
    is_new = True
    motor = False

    def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas, 
                 _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso):
        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo 
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.capacidad_tanque = 25

    # if self.variable == False:  ==== if not self.variable:
    # if self.variable == True:   ==== if self.variable:

    def arrancar(self):
        # if self.motor == True:        
        #   print("El motor ha arrancado")
        # if self.motor == False:
        #   print("El motor ya estaba en marcha")

        # if self.motor:        
        #   print("El motor ha arrancado")
        # if not self.motor:
        #   print("El motor ya estaba en marcha")

        if not self.motor:
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha")

    def detener(self):
        if not self.motor:
            print("El motor ya estaba detenido")
        else:
            print("El motor se ha apagado")
    
    def consultar_precio(self):
        print(f'El precio de la motocicleta {moto1.marca} {moto1.modelo} es de {moto1.precio}$')

    def consultar_capacidad_combustible(self):      
        print(f'La capacidad de combustible que tiene la motocicleta {moto_2.marca} {moto_2.modelo} es de {moto_2.combustible_litros} LT')


moto1 = Motocicleta("Negro", "XX22", 10, 2, "Kawasaki", "Ninja", "03/10/2023", 200, 120)

moto_2 = Motocicleta(_matricula="XXX-126", _combustible_litros=0, _color="Negra", _marca="ZONTES", _modelo="V-310", 
                     _numero_ruedas=2, _peso=150, _fecha_fabricacion="19/09/2023", _velocidad_punta=150)

moto1.arrancar()
moto1.detener()
moto1.precio = 9000
print(f'El precio de la motocicleta {moto1.marca} {moto1.modelo} es de {moto1.precio}$')
moto1.consultar_precio()
moto_2.consultar_precio()

# crear un método que permita comprobar la cantidad de combustible
