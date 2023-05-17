

class Artefacto:
    def __init__(self, name, nivel_de_ki):
        self.__name = name
        self.__nivel = nivel_de_ki
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.name__name = name

    @property
    def nivel_de_ki(self) -> float:
        return self.__nivel
    
    @nivel_de_ki.setter
    def nivel_de_ki(self, nivel_de_ki: float) -> None:
        self.__nivel = nivel_de_ki

vicente = Artefacto("vicente", 10000.2)
print(vicente.name)
print(vicente.nivel_de_ki)


#ejemplos de compañeros
