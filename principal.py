def pedir_numero():
    num = 0

    while True:
        try:
            num = int(input("Ingrese un número entero positivo para calcular su factorial: "))
            if num >= 0:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    return num

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def suma_primeros_n(n):
    if n <= 0:
        return 0
    else:
        return n + suma_primeros_n(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1 - Factorial")
    print("2 - Suma de los primeros n números")
    print("3 - Calcular n-ésimo numro de Fibonacci")
    print("4 - Contar letra en una palabra")
    print("5 - Invertir una cadena de texto")
    print("6 - Calcular potencia")
    print("0 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Resultado: {factorial(pedir_numero())}")

    elif opcion == "2":
        print(f"Resultado: {suma_primeros_n(pedir_numero())}")
    elif opcion == "3":
        print(f"Resultado: {fibonacci(pedir_numero())}")
    elif opcion == "4":
        print()
