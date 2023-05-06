class Droid:
    def __init__(self, name):
        self.hidden__name = name
    
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self__name = name
    
arturo = Droid("Arturo")

print(arturo.name)