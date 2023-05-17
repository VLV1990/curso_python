class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.apps = []
        self.status = False
        self.num_cores = num_cores

    def power_on(self):
        print("hello")
        self.status = True

    def power_off(self):
        print("good bye")
        self.power_on = False

    def power_on(self):
        self.status = True 
        print("celular prendido")

    def power_off(self):
        self.status = False

    def install_app(self, app):
        self.apps.append(app)
        print("Installing", app, "was successful")
    
    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
            print("The app was uninstalled successfully")

cel = MobilePhone('china', 7.5 , 8)
print("caracteristicas")

cel.power_on()
print("holahola", "cel.power_on")

cel.install_app("Whazap")
cel.install_app('facebook')
print("apps instalada", cel.apps)

cel.power_off()
     