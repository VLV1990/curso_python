class Cuenta_de_Banco:
    def __init__(self, _cliente, _cuenta, _saldo, _movimiento, _fechaMovimiento, _montoMovimiento):
        self.cliente = _cliente
        self.cuenta = _cuenta
        self.saldoInicial = 100
        self.movimiento = _movimiento
        self.fecha = _fechaMovimiento
        self.monto = _montoMovimiento
        self.saldo = _saldo




def depositar(self):
        _montoMovimiento = float(input("Ingrese el monto que desea depositar :"))
        if _montoMovimiento >= 1:
            print("su saldo se ha depositado exitosamente")
            print(f"su nuevo saldo es {self.saldoInicial + _montoMovimiento}.")
        else:
            print('monto no aceptado')

def retirar(self):
        _montoMovimiento = float(input('Ingreso el monto que desea retirar'))
        if _montoMovimiento <= self.saldo:
            print("su retiro se ha efectuado de manera exitosa")
            print(f"su nuevo saldo es {self.saldo - _montoMovimiento}")
        else:
            print("monto no aceptado, escriba otra cifra")

transaccion1 = Cuenta_de_Banco("James Bond", "007", "1000", 1 , "2023-04-28",5000)

transaccion1.depositar()



# Crear una cuenta bancaria


# Realizar algunas transaccionescuenta1.depositar(1000, "2022-04-28")



# Obtener el estado de cuenta
