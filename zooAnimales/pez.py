from zooAnimales.animal import Animal
class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, cantidadAletas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad

    def getCantidadAletas(self):
        return self._cantidadAletas