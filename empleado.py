from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, genero, edad, ciudad,pais, sueldo):
        Persona.__init__(self, nombre, genero, edad, ciudad, pais)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, value):
        self._sueldo = value

if __name__ == '__main__':
    emp1 = Empleado("Mario", "M", 25, "Guayaquil",'Ecuador', 500)
    print(emp1)