class Persona:
    def __init__(self, ape_pat, ape_mat, nom):
        self.apellido_paterno = ape_pat
        self.apellido_materno = ape_mat
        self.nombres = nom

    def nombre_completo(self):
        '''Imprime el nombre completo de la persona'''
        print(f'{self.apellido_paterno} {self.apellido_materno}, {self.nombres}')


class Estudiante(Persona):
    def __init__(self, ape_pat, ape_mat, nom, carr):
        
        # Pasar argumentos requeridos por la clase Persona:
        super().__init__(ape_pat, ape_mat, nom)
        
        # Añadir atributo particular para la clase Estudiante:
        self.carrera = carr

    def nombre_completo(self):
        '''Imprime el nombre completo y carrera del estudiante'''
        super().nombre_completo()
        print(f'Estudiante de {self.carrera}')


# Instanciar con el mismo constructor que Persona:
estudiante_1 = Estudiante('Vivero', 'Alarcón', 'Guillermo', 'Minas')

# Pedir el nombre completo del estudiante:
estudiante_1.nombre_completo()

# Imprimir la carrera del estudiante:
print(estudiante_1.carrera)