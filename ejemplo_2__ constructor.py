class Persona:

    # 1. Atributos de clase:
    especie = 'humana'

    # 2. Atributos de instancia (estado inicial):
    def __init__(self, nom, ape, edad, dorm):
        self.nombre = nom
        self.apellido = ape
        self.edad = edad
        self.dormido = dorm

    # 3. Funcionalidades o métodos:
    def despertar(self):
        self.dormido = False
        print('¡Buenos días!')


# 4. Instanciar pasando los valores iniciales:
persona_1 = Persona('Guillermo', 'Vivero', 28, False)
print(persona_1.nombre)

# 5. Crear una segunda instancia:
persona_2 = Persona('Nicolás', 'Alarcón', 27, True)
print(persona_2.nombre)