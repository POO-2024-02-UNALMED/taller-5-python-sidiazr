from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, pelaje = None, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)
    
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas