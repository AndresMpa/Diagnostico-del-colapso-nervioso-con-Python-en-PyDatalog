from Controler import qac_from_kbd, is_this_random_
from Users import checkup, add_new_user
from Ui import welcome, user_menu_check_in, menu_error, user_have_checked_up

welcome()
user_menu_check_in()
op = 1

while op < 3:
    menu_error()
    user_menu_check_in()
    op = int(input("\n\t\tIngresa tu elección aquí: "))
    if op == 1:
        DNI = input("INGRESA TU NOMBRE DE USUARIO:\t")
        password = input("\nINGRESA TU CONTRASEÑA:\t")
        is_this_random_(checkup(DNI, password))
    elif op == 2:
        add_new_user()
    elif op == 3:
        qac_from_kbd()
    elif op == 4:
        user_have_checked_up()