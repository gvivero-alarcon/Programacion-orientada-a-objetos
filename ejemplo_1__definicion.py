class Persona:

    # 1. Características o atributos de clase:
    nombre = ''
    apellido = ''
    edad = 0
    dormido = True

    # 2. Funcionalidades o métodos:
    def despertar(self):

        # Todo atributo o método se accede con SELF:
        self.dormido = False

        # Imprimir un saludo de buenos días:
        print('¡Buenos días!')


# 3. Crear una instancia u objeto:
persona_1 = Persona()

# 4. Asignar apellido a la persona:
persona_1.apellido = 'Vivero'
print(persona_1.apellido)

# 5. Despertar a la persona:
persona_1.despertar()
print(persona_1.dormido)

# 6. Crear un segundo objeto persona:
persona_2 = Persona()
persona_2.apellido = 'Alarcón'

# 7. El objeto se inicia con los valores por defecto:
print(persona_2.apellido)
print(persona_2.dormido)