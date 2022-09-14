def add_descripcions():
    medicines = open('description_of_medications.txt', 'a+')

    ids = input("Ingresa el numero de identificación del producto: \n")
    name = input("Ingresa el nombre del medicamento: \n")
    types = input("Ingresa el tipo de medicamento: \n")
    quantity = input("Ingresa la cantidad de medicamento por recipiente: \n")
    info = input("Ingresa la descripción del medicamento: \n")

    descripcions = dict(id=ids, medicine_name=name, medicine_type=types, medicine_quantity=quantity, descripcion=info)

    medicines.write(descripcions)
    medicines.close()

def look_for_descriptions(id, name_or_id):
    descripcions = open('description_of_medications.txt', 'r')

    if name_or_id == 1:
        for i in descripcions:
            if descripcions["medicine_name"][i] == id:
                print("Numero de identificación: "+descripcions["id"][i]+"\n")
                print("Nombre del medicamento: "+descripcions["medicina_name"][i]+"\n")
                print("Tipo de medicamento: "+descripcions["medicine_type"][i]+"\n")
                print("Descripción del medicamento: "+descripcions["description"][i]+"\n")
    else:
        if name_or_id == 2:
            for i in descripcions:
                if descripcions["id"][i] == id:
                    print("Numero de identificación: " + descripcions["id"][i] + "\n")
                    print("Nombre del medicamento: " + descripcions["medicina_name"][i] + "\n")
                    print("Tipo de medicamento: " + descripcions["medicine_type"][i] + "\n")
                    print("Descripción del medicamento: " + descripcions["description"][i] + "\n")