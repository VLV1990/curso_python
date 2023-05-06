# Escriba una clase MobilePhone que represente un telefono movil.
# Atributos
# manufacturer ( cadena de texto)
# screen_size (flotante)
# apps (lista de cadenas de texto)
# status (false: apagado, True: encendido)
# Metodos
# _init_(self, manufacturer, screen_size, num:cores)
#power_on(self)
#power_off(self)
# install_app(self, app)
#uninstall_app(dels, app)



class MobilePhone:
    def _init_(self):
        self.power_on = False
    def switch_on(self):
        print("apagado")
        self.power_on = True
    def switch_off(self):
        print("bienvenido a samsung")
        self.power_off = False

#estancear la variable
samsung_phone = MobilePhone()
mac_phone = MobilePhone()

samsung_phone.switch_on()
print("bienvenido a samsung:", samsung_phone.power_on)
mac_phone.switch_off()
print("good bye!:", mac_phone.power_off)
samsung_phone.switch_off()
print(samsung_phone.power_on)