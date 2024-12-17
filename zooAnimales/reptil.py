from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, largoCola = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largo):
        self._largoCola = largo

    def getLargoCola(self):
        return self._largoCola