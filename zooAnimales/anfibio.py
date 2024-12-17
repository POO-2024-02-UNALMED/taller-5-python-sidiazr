from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado = []
    salamandras = 0
    ranas = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPiel = None, venenoso = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)
    
    
    def setColorPiel(self, color):
        self._colorPiel = color

    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def isVenenoso(self):
        return self._venenoso