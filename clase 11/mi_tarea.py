import datetime


class Torniquete:
    def __init__(self, pasajero):
        self.tipo_pasajero = pasajero
        self.fecha_hoy = datetime.date.today()
        self.costo = 730
        self.total_recaudado = 0


    def acceso(self):
        tipo_pasajero = input('Tipo de pasajero: ')
        if tipo_pasajero == "menor":
            print(f"el valor de su pasajer es : {float(00)}")
        elif tipo_pasajero == "adulto mayor":
            print(f"el valor de su pasaje es : {self.costo * 0.5}")
            
        else:
            print(f"el valor de su pasaje es : {float(self.costo)}")

    def recaudacion_diaria(self):
        print(f'la recaudacion diaria al dia {self.fecha_hoy} fue de {float(0)}')

for i in range(5):
    pasajero = Torniquete("pasajero")
    pasajero.acceso()

        

pasajero = Torniquete("pasajero")
pasajero.acceso()
pasajero.recaudacion_diaria()