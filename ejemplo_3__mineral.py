class Mineral:
    def __init__(self, name, color, hardness, density):
        self.name = name
        self.color = color
        self.hardness = hardness
        self.density = density

    def get_name(self):
        '''Recupera el nombre asignado al mineral'''
        print(f'Este mineral se llama {self.name}')

    def get_density(self):
        '''Recupera la densidad del mineral'''
        print(f'La densidad de {self.name} es {self.density} g/cm\u00b3')

    def volume(self, tonnage):
        '''Calcula el volumen ocupado por un tonelaje dado de mineral'''
        volume = tonnage / self.density
        print(f'{tonnage} t de {self.name} ocuparán {volume:.2f} m\u00b3')


# 1. Inicializar los objetos:
chalcopyrite = Mineral('Calcopirita', 'Amarillo', 4, 4.1)
magnetite = Mineral('Magnetita', 'Pardo', 6, 5.0)

# 2. La variable nombre de cada clase es almacenada:
print(chalcopyrite.name)
print(magnetite.name)

# 3. Podemos definir una función que nos devuelva el nombre:
chalcopyrite.get_name()
magnetite.get_name()

# 4. También podemos imprimir la densidad y su unidad:
chalcopyrite.get_density()
magnetite.get_density()

# 5. Agregamos funciones que calculan volúmenes:
chalcopyrite.volume(100)
magnetite.volume(100)

# 6. No hay necesidad de definir múltiples variables:
if chalcopyrite.hardness > magnetite.hardness:
    print('La calcopirita es más dura que la magnetita')
else:
    print('La magnetita es más dura que la calcopirita')
