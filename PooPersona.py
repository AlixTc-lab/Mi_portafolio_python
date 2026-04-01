# Clase Persona con atributos y métodos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo
        self.edad = edad      # atributo

    # Método para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creamos objetos de la clase Persona
persona1 = Persona("Ana", 20)
persona2 = Persona("Luis", 25)

# Llamamos al método saludar de cada objeto
persona1.saludar()
persona2.saludar()