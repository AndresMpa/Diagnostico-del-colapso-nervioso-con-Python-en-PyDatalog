from pyDatalog import pyDatalog

# CONOCIMIENTO

pyDatalog.create_terms('padre, madre, abuelos_paternos, abuelos_maternos')

# REGLAS

pyDatalog.create_terms('abuelos_paternos, abuelas_paternas')

# VARIABLES

pyDatalog.create_terms('Abuelo, Abuela, Padre, Nieto')

# PADRES

+ padre('Juan', 'Carlos')
+ padre('Juan', 'Rosario')
+ padre('Juan', 'Soltero')
+ padre('Victor', 'Belen')
+ padre('Carlos', 'Elena')
+ padre('Carlos', 'Carlitos')

# MADRES

+ madre('Maria', 'Soltero')
+ madre('Maria', 'Carlos')
+ madre('Maria', 'Rosario')
+ madre('Consuelo', 'Belen')
+ madre('Belen', 'Elena')
+ madre('Belen', 'Carlitos')

# ABUELOS PATERNOS

abuelos_paternos(Abuelo, Nieto) <= padre(Abuelo, Padre) & padre(Padre, Nieto)

abuelas_paternas(Abuela, Nieto) <= madre(Abuela, Padre) & madre(Padre, Nieto)


def buscar_abuelos():
    abuelo_a_buscar = input("Ingrese el nombre del abuelo que busca: ")
    abuelo_encontrado = abuelos_paternos(abuelo_a_buscar, Nieto)
    print(abuelo_encontrado)


def buscar_abuelas():
    abuela_a_buscar = input("Ingrese el nombre del abuelo que busca: ")
    abuela_encontrado = abuelas_paternos(abuela_a_buscar, Nieto)
    print(abuela_encontrado)
