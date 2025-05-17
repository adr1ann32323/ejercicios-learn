import os
os.system("clear")
biblioteca = {
    155: {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    150: {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949}
}

#-------------funciones---------
#-------------funcion 1---------

def crear():
    try:
        nuevo_id = int(input("Ingresa el ID del nuevo libro: "))
        if nuevo_id in biblioteca:
            print("El ID del libro ya existe, debes agregar otro que no exista")
        
        else: 
            titulo= input("ingresa el nombre del libro: ").strip()
            autor = input("ingresa el nombre del autor: ").strip()
            if not titulo or not autor:
                print("los espacios para nombre y autor no pueden estar vacios")
            else:
                año= int(input("ingresa el año del libro"))
                if año < 1500:
                    print("solo puedes agregar libros del año 1500 en adelante")
                    
                else:
                    biblioteca[nuevo_id]={'titulo': titulo, 'autor': autor, 'año': año}
                    print("libro agregado correctamente")
                    print(f"ID: {nuevo_id} | Título: {biblioteca[nuevo_id]["titulo"]} | Autor: {biblioteca[nuevo_id]["autor"]} | Año: {biblioteca[nuevo_id]["año"]}")
    except:
        print("solo puedes ingresar numeros")
#----------------funcion 2--------------
def ver():
    if biblioteca:
            print("\nLibros disponibles en la biblioteca:")
            for id_libro, datos in biblioteca.items():
                print(f"ID: {id_libro}, Título: {datos['titulo']}, Autor: {datos['autor']}, Año: {datos['año']}")
    else:
        print("no hay libros en la biblioteca")

#------------------funcion 3-------------
def buscar():
    try:
        buscar = int(input("Ingresa el ID del libro que deseas buscar: "))
        if not buscar:
            print("el espacio para ID  no puede esatr vacio")
        else:
            if buscar in biblioteca:
                print(f"el libro si esta en la biblioteca")
                print(f"ID: {buscar} | Título: {biblioteca[buscar]["titulo"]} | Autor: {biblioteca[buscar]["autor"]} | Año: {biblioteca[buscar]["año"]}")
            else:
                print("Libro no encontrado.")
    except:
        print("solo puedes ingresar numeros")


#-------------funcion 4------------
def actualizar():
    try:
        actualizar = int(input("ingresa el ID del libro para actualizar: "))
        if not actualizar  in biblioteca:
            print("libro no encontrado, no se puede actualizar")
        else :
            new_autor =  input("ingresa el nuevo autor del libro: ").strip()
            if not new_autor:
                print("el espacio para autor no debe estar vacio")
            else:
                new_año= int(input("ingresa el nuevo año del libro: "))
                if new_año < 1500:
                    print("solo puedes ingresar libros del año 1500 en adelante")
                else:
                    biblioteca[actualizar]["autor"]= new_autor
                    biblioteca[actualizar]["año"]= new_año  
                    print(f"ID: {actualizar} | Título: {biblioteca[actualizar]["titulo"]} | Autor: {biblioteca[actualizar]["autor"]} | Año: {biblioteca[actualizar]["año"]}")
    except:
        print("solo puedes ingresar numeros")    
#------------funcion 5----------
def eliminar():
    try:
        eliminar= int(input("ingresa el ID del libro que deseas eliminar: "))
        if eliminar in biblioteca:
            biblioteca.pop(eliminar)
            print(f"el libro se elimino correctamente")
        else:
            print("el libro no se encuenta en la biblioteca")
    except:
        print(" solo puedes ingresar numeros en el ID")

#-------------funcion 6
def salir():
    print("gracias por usar el programa")
    print("Hasta pronto")
    
            
while True:
    print("\n---------------Biblioteca digital\n-------------")
    print("menu principal\n")
    print("1. Agregar un libro")
    print("2. Mostrar todos los libros")
    print("3. Buscar un libro por ID")
    print("4. Actualizar información de un libro")
    print("5. Eliminar un libro")
    print("6. Salir")
    
    opcion = input("Selecciona una opción (1-6): ") 
    match opcion:
        case "1":
            print("Agregar un libro")
            crear()
            
        case "2":
            print("Mostrar todos los libros")
            ver()
            
        case "3":
            print("Buscar un libro por ID")
            buscar()
        case "4":
            print("Actualizar información de un libro")
            actualizar()
            
        case "5":
            print("Eliminar un libro")
            eliminar()
            
        case "6":
            salir()
            break
        
        case _:
            print("opcion invalida, solo puedes ingresar de 1 - 6")                    
        