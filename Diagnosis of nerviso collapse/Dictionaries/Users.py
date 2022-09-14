def same_password(word_1, word_2):
    if word_1 == word_2:
        return 1
    else:
        return 0


def add_new_user():
    diccionarios = open('users_info.txt', 'a+')

    name = input("Ingresa tus nombres: \n")
    last_name = input("Ingresa tus apellidos: \n")
    dni = input("Ingresa tu cédula o número de identifiación: \n")
    e_mail = input("Ingresa tu correo: \n")
    f_pass_word = input("Ingresa tu contraseña: \n")
    s_pass_word = input("Vuelve a ingresar tu contraseña: \n")
    while same_password(f_pass_word, s_pass_word) != 1:
        print("\nLa contraseña y su confirmación no son la smisma, por favor ingresalas de nuevo:\n\n")
        f_pass_word = input("Ingresa tu contraseña: \n")
        s_pass_word = input("Vuelve a ingresar tu contraseña: \n")

    user = dict(nombre=name, apellido=last_name, user_id=dni, email=e_mail, password=pass_word)

    diccionarios.write(user)
    diccionarios.close()


# Valida si el usuario ingresado existe o no
def checkup(user_id, password):
    global step
    user = open('users_info.txt', 'r')
    progress = 1
    while progress != 0:
        step = 0
        users_id = 0
        user_password = 0
        for i in user:
            if user['user_id'][i] != user_id:
                pass
            else:
                users_id = 1

            if user['password'][i] != password:
                pass
            else:
                user_password = 1

        if users_id == user_password:
            step = 0
        else:
            step = 1

        if step == 1:
            progress = input("¿Algo no está bien deseas volver a ingresar tus datos? <1 Si>, <0 No>")
        else:
            progress = 0

    return step
