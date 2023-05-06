#programacion orientada a objetos
#objetos -> clases, desde ahora lo conoceremos asi. 
#beneficios: 
#* encapsulamiento - clase_BL
#                  - clase_BB
#                  - clase_KEN

#Abstraccion: 
#* generalizacion de algo
# CLASE = molde de donde se producen objetos

#sintansis : (UpperCamelCase)
#CLASS NombreCLASE: 
class Transporte:
    pass
#instanciar la clase y crear un objeto "llamrla para que a partir de eso SE PUEDA CREAR"
transporte1 = Transporte()
transporte2 = Transporte()
transporte3 = Transporte()
transporte4 = Transporte()

class BuzzeLightYear:
    pass

bozz1 = BuzzeLightYear()
bozz2 = BuzzeLightYear()

print(type(transporte1))
print(type(bozz1))

class Droid: #es un metodo , no le vamos a dar una nombre, sino una notacion. 
    def _init_(self):
        self.power_on = False
    def switch_on(self):
        print("hola soy un droide, y estoy a tus ordenes")
        self.power_on = True
    def switch_off(self):
        print("hasta la vista, baby!")
        self.power_off = False

#estancear la variable
k8_arthur = Droid()
k8_tripio = Droid()

k8_arthur.switch_on()
print("power on arthur:", k8_arthur.power_on)
k8_tripio.switch_off()
print("power on tripio:", k8_tripio.power_off)
k8_arthur.switch_off()
print(k8_arthur.power_on)


#Funciones y atributos

class Vehicle:
    def __init__(self, type, model):
        self.type_Vehicle = type
        self.model_Vehicle = model

sedan = Vehicle('sedan', 'aveo')
print(sedan.type_Vehicle, sedan.model_Vehicle)
pickup = Vehicle('pickup', 'ranger')
print(pickup.type_Vehicle, pickup.model_Vehicle)
    

# ¿ como saber cuando el robot esta encendido, y cuando esta apagado ?
