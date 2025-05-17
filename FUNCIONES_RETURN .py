# Nivel Básico


def saludo_personalizado(nombre):  
    return f"Hola, {nombre}! Bienvenido." 


def suma_dos_numeros(a, b): 
    return a + b  


def es_par_o_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar" 


def es_mayor_de_edad(edad):  
    return "Mayor de edad" if edad >= 18 else "Menor de edad"  


def celsius_a_fahrenheit(celsius):  
    return celsius * 9/5 + 32  


def area_triangulo(base, altura):  
    return (base * altura) / 2  

def mayor_de_lista(lista_numeros):  
    return max(lista_numeros) 

def contar_letras(palabra, letra):  
    return palabra.count(letra)  

# Nivel Intermedio

def filtrar_pares(lista_numeros): 
    return [num for num in lista_numeros if num % 2 == 0]  

#---------------INICIA-----------
#llamar funcion

filtrar_pares()