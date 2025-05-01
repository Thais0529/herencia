from persona import Persona

class Empleado (Persona):
    def __init__(self, nombre, genero, edad, ciudad, sueldo,pais):
        Persona.__init__(self, nombre, genero, edad, ciudad, pais)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, value):
        self._sueldo = value


emp1 = Empleado(nombre='Luis', genero='M', edad=22, ciudad='guayaquil',pais='Ecuador',sueldo=500)
print(emp1)
