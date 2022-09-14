from pyDatalog import pyDatalog

pyDatalog.create_terms('enfermedad, sintomas')

#PRINCIPALES ENFERMEDADES

+ enfermedad('antracnosis', 'hortalizas')
+ enfermedad('alternaria', 'hortalizas')
+ enfermadad('botrytis', 'hortalizas')
+ enfermedad('damping-off', 'hortalizas')
+ enfermedad('pudricion blanca de la cebolla', 'hortalizas')
+ enfermedad('hernia de las crucíferas', 'hortalizas')
+ enfermedad('mancha de anillo u ojo de sapo', 'hortalizas')
+ enfermedad('esclerotiniasis', 'hortalizas')

#SINTOMAS

+ sintomas('manchas color pardo oscuro', 'antracnosis')
+ sintomas('lesiones cóncavas con una masa gelatinosa de color rojizo o salmón en su interior', 'antracnosis')
+ sintomas('moho de color gris y de aspecto aterciopelado', 'antracnosis')

+ sintomas('formación de anillos concéntricos de color púrpura sobre las hojas', 'alternaria')
+ sintomas('pudrición en el cuello de la raíz de la planta', 'alternaria')

+ sintomas('manchas cloróticas', 'botrytis')

+ sintomas('amarillamiento en las hojas', 'damping-off')
+ sintomas('doblamiento del tallo', 'damping-off')

+ sintomas('retraso en el crecimiento', 'pudricion blanca de la cebolla')

+ sintomas('pudrición de semillas, agallas y tumores en el cuello del tallo y las raíces', 'hernia de las crucíferas')
+ sintomas('reducción del tamaño de las plantas y marchitamiento de las hojas exteriores durante horas o días calurosos', 'hernia de las crucíferas')

+ sintomas('formación de lesiones redondas de color gris oscuro', 'mancha de anillo u ojo de sapo')

+ sintomas('pudrición acuosa en la base del tallo de las plántulas', 'esclerotiniasis')
+ sintomas('pudrición húmeda y blanca del tallo', 'esclerotiniasis')

def listar_enfermedades():
    caso = list(enfermedades(Enfermedaes, 'hortalizas'))
    for item in caso:
        diagnostico(caso[item])

def diagnostico(Caso):
    tupla_de_enfermedades = sintomas(Sintoma, Caso)
    enfermedades = list(tupla_de_enfermedades)
    suma = 0
    for item in enfermedades:
        cuadro = input("¿La enfermedad "+enfermedades[item]+"? <1 si> <0 no>")
        if cuadro == 1:
            suma += 1
    if suma == len(enfermedades):
        print("La planta presenta "+caso+"\n")