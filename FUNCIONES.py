#funciones Basicas

def positivo_negativo_cero():
    n = float(input("Ingresa un numero: "))
    if n > 0:
        print("Es positivo")
    elif n < 0:
        print("Es negativo")
    else:
        print("Es cero")

def par_o_impar():
    n = int(input("Ingresa un numero: "))
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def mayor_de_dos():
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    if a > b:
        print(f"{a} es mayor")
    elif b > a:
        print(f"{b} es mayor")
    else:
        print("Son iguales")

def clasificacion_edad():
    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        print("Edad no válida")
    elif edad <= 12:
        print("Niño")
    elif edad <= 17:
        print("Adolescente")
    elif edad <= 64:
        print("Adulto")
    else:
        print("Anciano")

def aprobado_reprobado():
    calif = float(input("Calificacion (0-10): "))
    if calif >= 6:
        print("Aprobado")
    else:
        print("Reprobado")

def multiplo_3_5():
    n = int(input("Ingresa un numero: "))
    if n % 3 == 0 and n % 5 == 0:
        print("Es múltiplo de 3 y 5")
    elif n % 3 == 0:
        print("Es múltiplo de 3")
    elif n % 5 == 0:
        print("Es múltiplo de 5")
    else:
        print("No es multiplo de 3 ni de 5")

def mayor_de_tres():
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    c = float(input("Tercer numero: "))
    mayor = max(a, b, c)
    print(f"El mayor es: {mayor}")

def calculadora_simple():
    a = float(input("Primer numero: "))
    op = input("Operador (+, -, *, /): ")
    b = float(input("Segundo numero: "))
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b if b != 0 else "No se puede dividir entre cero")
    else:
        print("Operador invalido")

def año_bisiesto():
    anio = int(input("Ingresa un año: "))
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

def validar_contrasena():
    contrasena = "python123"
    intento = input("Ingresa la contraseña: ")
    if intento == contrasena:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

#  funciones intermedias

def contar_1_10():
    for i in range(1, 11):
        print(i)

def contador_descendente():
    numero = 10
    while numero >=1:
        print(numero)
        numero -= 1

def sumar_n_numeros():
    n = int(input("¿Cuántos numeros sumar?: "))
    suma = 0
    for i in range(1, n+1):
        suma += i
    print(f"Suma: {suma}")

def tabla_multiplicar():
    numero = int(input("¿Tabla de que numero?: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")

def suma_hasta_numero():
    n = int(input("Sumar del 1 hasta: "))
    suma = sum(range(1, n+1))
    print(f"Suma: {suma}")

def numero_secreto():
    import random
    secreto = random.randint(1, 100)
    intento = None
    while intento != secreto:
        intento = int(input("Adivina el numero (1-100): "))
        if intento < secreto:
            print("Demasiado bajo")
        elif intento > secreto:
            print("Demasiado alto")
    print("¡Correcto!")

def cuenta_regresiva_pausa():
    import time
    n = int(input("Cuenta regresiva desde: "))
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("¡Despegue!")

def multiplos_3_1_100():
    for i in range(3, 101, 3):
        print(i)

def factorial_numero():
    n = int(input("Número para factorial: "))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"Factorial: {fact}")

def piramide_asteriscos():
    n = int(input("Altura de la pirámide: "))
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))

#  funciones avanzadas

def suma_elementos_lista():
    nums = []
    while True:
        val = input("Número (o 'fin' para terminar): ")
        if val == "fin":
            break
        nums.append(float(val))
    print(f"Suma: {sum(nums)}")

def buscar_en_lista():
    lista = input("Escribe elementos separados por espacios: ").split()
    elem = input("Elemento a buscar: ")
    if elem in lista:
        print("Está en la lista")
    else:
        print("No está en la lista")