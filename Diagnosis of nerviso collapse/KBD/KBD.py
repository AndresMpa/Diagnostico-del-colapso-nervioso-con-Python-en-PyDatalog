from pyDatalog import pyDatalog

# CONOCIMIENTO
pyDatalog.create_terms('sintomas, causas, tratamiento, medicina, tipo')

# REGLAS
pyDatalog.create_terms('sintomas_asociados_a_una_enfermedad')

# VARIABLES
pyDatalog.create_terms('Enfermedad, Sintomas')

# SINTOMAS COLAPSO NERVIOSO

+ sintomas('Colapso nervioso', 'Ansiedad')
+ sintomas('Colapso nervioso', 'Depresion')

# SUBSINTOMAS ANSIEDAD

+ sintomas('Ansiedad', 'Tension en el cuello')
+ sintomas('Ansiedad', 'Tension en los hombros')
+ sintomas('Ansiedad', 'Tension en la espalda')
+ sintomas('Ansiedad', 'Dificultades de respiracion')
+ sintomas('Ansiedad', 'Vision Nublada')
+ sintomas('Ansiedad', 'Sofoco')
+ sintomas('Ansiedad', 'Taquicardia')
+ sintomas('Ansiedad', 'Apresion en el pecho')
+ sintomas('Ansiedad', 'Sensacion de nudo en el estomago')
+ sintomas('Ansiedad', 'Nauseas')
+ sintomas('Ansiedad', 'Sudoracion')
+ sintomas('Ansiedad', 'Temblor')
+ sintomas('Ansiedad', 'Hormigueo en las manos')
+ sintomas('Ansiedad', 'Inestabilidad')
+ sintomas('Ansiedad', 'Entumecimiento en las piernas')
+ sintomas('Ansiedad', 'Exageracion a los problemas')
+ sintomas('Ansiedad', 'Preocupacion excesiva')
+ sintomas('Ansiedad', 'Insomnio')

# SUBSINTOMAS DEPRESION

+ sintomas('Depresion', 'Pensamientos suicidas')
+ sintomas('Depresion', 'Tristaza frecuente')
+ sintomas('Depresion', 'Irritabilidad')
+ sintomas('Depresion', 'Llanto frecuente')
+ sintomas('Depresion', 'Altibajos Emocionales')
+ sintomas('Depresion', 'Culpa')
+ sintomas('Depresion', 'Deesperanza')
+ sintomas('Depresion', 'Placer en realizar actividades realizadas con tristeza')
+ sintomas('Depresion', 'Falta de concentracion')
+ sintomas('Depresion', 'Baja autoestima')

# CAUSAS DEL COLAPSO NERVIOSO

+ causas('Colapso nervioso', 'Reaccion ezagerada a los problemas')
+ causas('Colapso nervioso', 'Consecuencia de un acontecimiento especialmente desagradable')
+ causas('Colapso nervioso', 'Aparicion de un problema mayor')
+ causas('Colapso nervioso', 'Acumulacion de pequeños problemas')
+ causas('Colapso nervioso', 'Rechazo')
+ causas('Colapso nervioso', 'Pensamientos negativos')

# NIVELES COLAPSO NERVIOSO

+ tipo('Colapso nervioso', 'Primer nivel')
+ tipo('Colapso nervioso', 'Segundo nivel')
+ tipo('Colapso nervioso', 'Tercer nivel')

# TIPOS DE DEPRESIÓN

+ tipo('Depresion', 'Episodio depresivo')
+ tipo('Depresion', 'Transtorno depresivo recurrente')
+ tipo('Depresion', 'Dismitia')
+ tipo('Depresion', 'Depresión bipolar')
+ tipo('Depresion', 'Depresión psicotica')
+ tipo('Depresion', 'Depresión atipica')
+ tipo('Depresion', 'Transtorno depresivo estacional')

# TIPOS DE ANSIEDAD

+ tipo('Ansiedad', 'Transtorno obsesivo compulsivo (TOC)')
+ tipo('Ansiedad', 'Transtorno de estrés post traumatico (TEPT)')
+ tipo('Ansiedad', 'Transtorno de pánico')
+ tipo('Ansiedad', 'Transtorno de ansiedad generalizada (TAD)')
+ tipo('Ansiedad', 'Fobia social')
+ tipo('Ansiedad', 'Agorafobia')
+ tipo('Ansiedad', 'Fobía especifica')

# TRATAMIENTOS DEL COLAPSO NERVIOSO

+ tratamiento('Colapso nervioso', 'Ejercicio fisico')
+ tratamiento('Colapso nervioso', 'Organizacion en los que haceres')
+ tratamiento('Colapso nervioso', 'Tiempo a solas')
+ tratamiento('Colapso nervioso', 'Proponerse objetivos realistas')
+ tratamiento('Colapso nervioso', 'Informarse sobre la enfermedad')
+ tratamiento('Colapso nervioso', 'Cambiar habitos')

# TRATAMIENTO FARMACOLÓGICO

+ medicina('Colapso nervioso', 'Benzodiazopinas (BZD)')
+ medicina('Colapso nervioso', 'Inhibidores selectivos de la recaptura de la serotonina')
+ medicina('Colapso nervioso',
           'Buspirona')  # Se usa en vez de la BZD si el paciente usó sustancias psicoactivas o esta consumiendo otro medicamento
+ medicina('Colapso nervioso', 'Antidepresivos')

# REGLAS

sintomas_asociados_a_una_enfermedad(Enfermedad, Sintomas) <= sintomas(Enfermedad, Sintomas)


# FUNCIONES PARA OBTENER LOS DATOS

def consulta_diriguida(Enfermeda_preestablecida):
    Sintomas_de_las_enfermedades_encontradas = sintomas_asociados_a_una_enfermedad(Enfermeda_preestablecida, Sintomas)
    print("Los sintomos de " + Enfermeda_preestablecida + " son: \n")
    print(Sintomas_de_las_enfermedades_encontradas)


def consultar_lista_de_enfermedades():
    enfermedades_del_sistema = sintomas_asociados_a_una_enfermedad('Colapso nervioso', Sintomas)
    print(enfermedades_del_sistema)


def diagnostico():
    tupla_de_sintomas_para_depresion = sintomas_asociados_a_una_enfermedad("Depresión", Sintomas)
    tupla_de_sintomas_para_ansiedad = sintomas_asociados_a_una_enfermedad("Ansieda", Sintomas)
    sintomas_de_la_depresion = list(tupla_de_sintomas_para_depresion)
    sintomas_de_ansiedad = list(tupla_de_sintomas_para_ansiedad)
    print("Indique cuidadosamente que sintomas presenta el paciente con un 1 y los que no con un 0\n\n")
    suma_depresion: int = 0
    suma_ansiedad: int = 0
    for i in sintomas_de_la_depresion:
        op = input("¿El paciente presenta " + sintomas_de_la_depresion[i] + "?\n")
        if op == 1:
            suma_depresion += 1
    for i in sintomas_de_ansiedad:
        op = input("¿El paciente presenta " + sintomas_de_ansiedad[i] + "?\n")
        if op == 1:
            suma_ansiedad += 1
    print("El paciente presenta un indice de depresión de "+suma_depresion+"%\n")
    print("El paciente presenta un indice de ansiedad de "+suma_ansiedad+"%\n")
    suma_depresion = suma_depresion * 0.7
    suma_ansiedad = suma_ansiedad * 0.3
    return (suma_depresion + suma_ansiedad)/100
