import datetime


class Cuenta_de_Banco:
    def __init__(self, cliente, cuenta, saldo_inicial):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo_inicial = saldo_inicial
        self.fecha_hoy = datetime.date.today()
        self.monto_movimiento = 0

    def depositar(self):
        monto_movimiento = float(
            input("Ingrese el monto que desea depositar: "))
        if monto_movimiento >= 1:
            print("Su saldo se ha depositado exitosamente.")
            self.saldo_inicial += monto_movimiento
            self.monto_movimiento = monto_movimiento
            print(f"Su nuevo saldo es {self.saldo_inicial}.")
        else:
            print('Monto no aceptado.')

    def retirar(self):
        monto_movimiento_retiro = float(
            input('Ingrese el monto que desea retirar: '))
        if monto_movimiento_retiro <= self.saldo_inicial:
            print("Su retiro se ha efectuado de manera exitosa.")
            self.monto_movimiento = monto_movimiento_retiro
            print(
                f"Su nuevo saldo es {self.saldo_inicial - monto_movimiento_retiro}.")
        else:
            print("Monto no aceptado. Escriba otra cifra.")

    def imprimir_estado_cuenta(self):
        print(
            f"Estado de cuenta de la cuenta {self.cuenta} a nombre de {self.cliente} es: ")
        print(f"fecha de hoy: {self.fecha_hoy}")
        print(f"su saldo actual es : {self.saldo_inicial + self.monto_movimiento}")

        while True:
            otra_operacion = input("¿Desea hacer otra operación? s/n ")
            if otra_operacion == "s":
                self.depositar()
                break
            elif otra_operacion == "n":
                break
            else:
                print("Opción no válida. Intente nuevamente.")


    

transaccion1 = Cuenta_de_Banco("James Bond", "007", 1000)

transaccion1.depositar()
transaccion1.retirar()
transaccion1.imprimir_estado_cuenta()
