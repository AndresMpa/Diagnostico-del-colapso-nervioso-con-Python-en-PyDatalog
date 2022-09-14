def bars(bars_num):
    for i in range(bars_num):
        print("\t\t|\t\t\t\t\t\t\t\t\t\t\t\t|")


def text_for_menu(string):
    print("\t\t|\t" + string + "\t|")


def welcome():
    print("\n\n\t\t________________________________________________")
    bars(5)
    print("\t\t|\t\t\tBIENVENIDO AL SISTEMA DE\t\t\t|")
    print("\t\t|\t\t\t DETECCIÓN DE COLAPSOS \t\t\t\t|")
    bars(4)
    print("\t\t|_______________________________________________|")


def user_menu_check_in():
    print("\n\n\t\t________________________________________________")
    bars(2)
    print("\t\t|\t\t\tHAS INGRESADO AL MENU DE \t\t\t|")
    print("\t\t|\t\t\t  INICIO DEL SISTEMA \t\t\t\t|")
    bars(1)
    print("\t\t|_______________________________________________|")
    bars(1)
    text_for_menu("1) Ingresa 1 para hacer el login\t\t")
    bars(1)
    bars(1)
    text_for_menu("2) Ingresa 2 para crear un usuario\t\t")
    bars(1)
    bars(1)
    text_for_menu("3) Ingresa 3 para hacer consultas al \t")
    text_for_menu("sistema\t\t\t\t\t\t\t\t\t")
    bars(1)
    bars(1)
    text_for_menu("4) Ingresa 4 para salir\t\t\t\t\t")
    bars(1)
    print("\t\t|_______________________________________________|")


def menu_error():
    print("\n\n\t\t________________________________________________")
    bars(2)
    print("\t\t|\t\t\tHAS DIGITADO UNA OPCIÓN QUE NO\t\t|")
    print("\t\t|\t\t\t\tEXISTE, REINGRESANDO \t\t\t|")
    bars(1)
    print("\t\t|_______________________________________________|")


def qac():
    print("\n\n\t\t________________________________________________")
    bars(2)
    print("\t\t|\t\t\tHAS INGRESA A LAS CONSULTAS\t\t\t|")
    print("\t\t|\t\t\t  DIRIGIDAS POR SISTEMA\t\t\t\t|")
    bars(1)
    print("\t\t|_______________________________________________|")
    bars(1)
    text_for_menu("1) Ingresa 1 para consultar enfermedades")
    bars(1)
    bars(1)
    text_for_menu("2) Ingresa 2 para consultar sintomas\t")
    bars(1)
    bars(1)
    text_for_menu("3) Ingresa 3 para tipos\t\t\t\t\t")
    bars(1)
    bars(1)
    text_for_menu("4) Ingresa 4 para salir\t\t\t\t\t")
    bars(1)
    print("\t\t|_______________________________________________|")


def user_login():
    print("\n\n\t\t________________________________________________")
    bars(2)
    print("\t\t|\t\t\tHAS INGRESADO AL LOGIN \t\t\t|")
    bars(1)
    print("\t\t|_______________________________________________|")
    bars(1)


def user_menu_options():
    print("\n\n\t\t________________________________________________")
    bars(2)
    print("\t\t|\t\t\tHAS INGRESADO AL MENU DE \t\t\t|")
    print("\t\t|\t\t\t OPCIONES DEL SISTEMA \t\t\t\t|")
    bars(1)
    print("\t\t|_______________________________________________|")
    bars(1)
    text_for_menu("1) Ingresa 1 para consultar el numero de ")
    text_for_menu("enfermedades registradas\t\t\t\t")
    bars(1)


def user_have_checked_up():
    print("\n\n\t\t________________________________________________")
    bars(5)
    print("\t\t|\t\t\tHAS SALIDO DEL SISTEMA DE\t\t\t|")
    print("\t\t|\t\t\t DETECCIÓN DE COLAPSOS \t\t\t\t|")
    bars(4)
    print("\t\t|_______________________________________________|")
