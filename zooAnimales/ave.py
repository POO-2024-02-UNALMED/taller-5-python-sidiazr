from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)
    

    def setColorPlumas(self, color):
        self._colorPlumas = color

    def getColorPlumas(self):
        return self._colorPlumas
    