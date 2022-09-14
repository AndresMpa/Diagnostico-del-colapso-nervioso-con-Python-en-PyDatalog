from pyDatalog import pyDatalog

pyDatalog.create_terms('enfermo, sintoma, elimina')

# REGLAS

pyDatalog.create_terms('como_curar')

# VARIABLES

pyDatalog.create_terms('Enfermo, Sintoma, Cura')

# ENFERMO

+ enfermo('manuel', 'gripe')

# SINTOMA

+ sintoma('alicia', 'cansancio')
+ sintoma('fiebre', 'gripe')
+ sintoma('tos', 'gripe')
+ sintoma('cansancio', 'anemia')

# CURA

+ elimina('vitaminas', 'cansancio')
+ elimina('aspirinas', 'fiebre')
+ elimina('jarabe', 'tos')

# REGLAS

como_curar(Enfermo, Cura) <= enfermo(Enfermo, Sintoma) & sintoma(Cura, Sintoma)

def curar_paciente():
    nombre_del_paciente = input('Ingrese el nombre del paciente: ')
    medicamentos = como_curar(nombre_del_paciente, Cura)
    print(medicamentos)

