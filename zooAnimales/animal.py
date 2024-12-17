


class Animal:
    _totalAnimales = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"Mamíferos: {Mamifero.cantidadMamiferos()} \nAves: {Ave.cantidadAves()} \nReptiles: {Reptil.cantidadReptiles()} \nPeces: {Pez.cantidadPeces()} \nAnfibios: {Anfibio.cantidadAnfibios()}"

    
    def __str__(self):
        if self._zona == None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, y mi genero es {self._genero}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.getZoo()}"
