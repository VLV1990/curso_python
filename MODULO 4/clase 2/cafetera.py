#declarando clases en python
class Taza:
    sizes = {
        "small": "pequeño",
        "medium": "mediano",
        "large" : "grande"
    }
    def __init__(self):
        self.size = self.sizes["small"]
class Maquina:
    def __init__(self,_tipo_cafe,_cantidad_agua,_cantidad_cafe):
        self.tipo_cafe = _tipo_cafe
        self.cantidad_agua = _cantidad_agua
        self.cantidad_cafe = _cantidad_cafe
        
class Cafe:
    tipo_cafe = {
        "arabico" : "arabico",
        "etiope" : "etiope",
        "colombiano" : "colombiano"
    }
    def __init__(self):
        self.tipo_cafe = self.tipo_cafe["arabico"]
class Leche:
    tipo_leche = {
        "entera" : "entera",
        "semi_descremada" : "semi_descremada",
        "descremada" : "descremada",
        "vegana":"vegana"
    }
    def __init__(self):
        self.tipo_leche = self.tipo_leche["entera"]
# instanciando una clase
