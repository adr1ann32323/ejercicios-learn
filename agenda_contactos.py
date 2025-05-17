agenda = {3006165814:{"nombre":"adrian arboleda","email":"adrian@gmail.com"},
          3008311657:{"nombre":"isabella pulgarin", "email":"isa102@gmail.com"},
          3000021202:{"nombre" :"papa", "email": ""}
}  
#---------------agregar--------------
def agregar():
    telefono= (input("ingresa el numero telefonico: "))
    
    if not telefono.isdigit():
        print("El número telefónico debe contener solo dígitos, sin ningun caracter o letras")
    elif telefono.startswith('0'):
        print("El número telefónico no puede iniciar con 0")
    elif len(telefono) < 7 or len(telefono) > 10:
        print("El número no debe tener menos de 7 ni más de 10 dígitos")
    elif int(telefono) in agenda:
        print("El número ya existe en la agenda")
    else:
        nombre = input("Ingresa el nombre: ").strip().lower()
        email= input("opcional, ingresa tu email: ")
        if not nombre:
            print("el espacio para nombre no debe estar vacio")
        elif nombre in agenda:
            print("el nombre ya existe en tu agenga")
        else:
            agenda[int(telefono)] = {"nombre": nombre,"email": email}
            print(f"el contacto se agrego correctamente")
            print(f"numero: {telefono} | nombre: {agenda[int(telefono)]["nombre"]} | email: {agenda[int(telefono)]["email"]}")
            
#------------------ver-----------------
def ver():
    if agenda:
        for contacto, datos in agenda.items():
            print(f"nombre: {datos["nombre"]} | numero: {contacto} | email: {datos["email"]}")
    else:
        print("no hay contactos en la agenga")
    
def buscar():
    nombre= input("ingresa el nombre del contacto: ").lower()
    encontrado=False
    for contacto, datos in agenda.items():
        if nombre  == datos["nombre"].lower():
            print(f'el contacto "{nombre}" se encuentra en la agenda')
            print(f"nombre: {datos["nombre"]} | numero: {contacto} | Email: {datos["email"]}")
            encontrado=True
            break
    if not encontrado:
        print(f'el contacto "{nombre}" no existe en la agenda')
#-------------actualizar--------------
def actualizar():
    actualizar=input("ingresa el nombre del contacto que deseas actualizar: ").strip().lower()
    encontrado=False
    for contacto, datos in agenda.items():
        if actualizar ==datos["nombre"].lower():
            print(f'el contacto "{actualizar}" se encuentra en la agenda')
            print(f"nombre: {datos["nombre"]} | numero: {contacto} | Email: {datos["email"]}")   
            nuevo_nombre=input("ingresa el nuevo nombre del contacto: ").strip().lower()
            if not nuevo_nombre:
                print("el espacio para nombre no debe estar vacio")
                encontrado=True
            else:
                nuevo_email=input("ingresa el nuevo email: ")
                agenda[contacto]["nombre"]= nuevo_nombre
                agenda[contacto]["email"]= nuevo_email
                print("el contacto se actualizo correctamente")
                print(f"nombre: {datos["nombre"]} | numero: {contacto} | Email: {datos["email"]}")
                encontrado=True
    if not encontrado:
        print(f'el contacto "{actualizar}" no existe en la agenda')  

#------------------Eliminar--------------------
def eliminar():
    eliminar= input("ingresa el nombre del contacto que deas eliminar: ").lower()
    encontrado=False
    clave_eliminar= None
    for contacto, datos in agenda.items():
        if eliminar == datos["nombre"].lower():
            clave_eliminar=contacto
            encontrado=True
    if encontrado:
        agenda.pop(clave_eliminar)
        print(f'el contacto "{eliminar}" se elimino correctamente')
    elif not encontrado:
        print(f'el contacto "{eliminar}" no existe en la agenda')
    
#----------------inicia----------------
while True:  
    print("\n------------Agenda de Contactos------------\n")
    print("1. Agregar un contacto")  
    print("2. ver todos los contactos")  
    print("3. Buscar un contacto por Nombre")  
    print("4. Actualizar un contacto")  
    print("5. Eliminar un contacto") 
    print("6. Salir")  
    
    opcion = input("Selecciona una opción (1-6): ") 

   
    match opcion:
        case '1':
            print("agregar contacto")
            agregar()
            
        case '2':
             print("lista de contactos")
             ver()

        case '3':
            print("buscar contacto por nombre")
            buscar()
            
        case '4':
            print("actualizar contacto")
            actualizar()

        case '5':
            print("eliminar contacto")
            eliminar()
            
        case '6':
            print("Hasta pronto")
            break
        case _:  
            print("Opción no válida. Intenta de nuevo.")