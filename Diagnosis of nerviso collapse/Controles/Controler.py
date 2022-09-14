from KBD import consultar_lista_de_enfermedades, diagnostico
from UI import qac, user_menu_options


def is_this_random_(user_have_logged):
    if user_have_logged != 0:
        print("No estas registrado en este sistema por ende no puedes acceder a las funciones de usuario, "
              "para solucionar esto registrate en el menu principal")
    else:
        indice_de_colapso = 0
        user_menu_options()
        op = input("\nIngresa la opción que deseas consultar: \t")
        if op == 1:
            consultar_lista_de_enfermedades()
        if op == 2:
            indice_de_colapso = diagnostico()
            print("El paciente presenta un indice de colapso de "+indice_de_colapso+"%")
        if op == 3:
            user_have_checked_up()



def qac_from_kbd():
    qac()
    op = int(input("Ingresa una opción para continuar"))
    if op < 0:
        exists = 0
    elif op > 4:
        exists = 0
    else:
        exists = 1
    while exists != 1:
        qac()
        op = int(input("\nLa opción ingresada no es contemplada dentro de las opciones de las que dispone, "
                       "ingrese una que si lo este: "))
        if op < 0:
            exists = 0
        elif op > 4:
            exists = 0
        else:
            exists = 1
    if op == 1:
        print("Dispones de las siguientes enfermedades para consultar: ")
        consultar_lista_de_enfermedades()
