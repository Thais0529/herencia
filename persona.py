class Persona:
    def __init__(self, nombre, edad, genero, ciudad, pais):
        # Atributos privados (encapsulados)
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self._ciudad = ciudad
        self._pais = pais

    # Métodos getter y setter para cada atributo
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa.")

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    def saludar(self):
        print(f"Hola, mi nombre es {self._nombre}, tengo {self._edad} años, soy {self._genero}, "
              f"vivo en {self._ciudad}, {self._pais}.")

    def __str__(self):
        # Usando __dict__ para obtener los atributos
        atributos = self.__dict__
        # Generando una cadena con los atributos
        return f"Persona({', '.join([f'{key[1:]}={value}' for key, value in atributos.items()])})"

if __name__ == '__main__':
    # Crear una instancia de Persona
    persona1 = Persona("Thais", 24, "femenino", "Guayaquil", "Ecuador")

    # Usar el método saludar
    persona1.saludar()

    # Modificar el nombre usando el setter
    persona1.nombre = "Thais Padilla"
    persona1.edad = 25  # Modificar edad usando el setter

    # Imprimir la representación del objeto con __str__
    print(persona1)

    # Imprimir el diccionario con __dict__
    print(persona1.__dict__)
