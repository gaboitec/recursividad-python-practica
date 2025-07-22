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


def contar_letra(palabra, letra):
    if not palabra:
        return 0
    else:
        if palabra[0] == letra:
            return 1 + contar_letra(palabra[1:], letra)
        else:
            return 0 + contar_letra(palabra[1:], letra)

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

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
        palabra = input("Ingrese una palabra: ")

        while True:
            letra = input("Ingrese la letra a contar: ")
            if len(letra) == 1:
                break
            else:
                print("Por favor, ingrese solo una letra")

        print(f"Resultado: {contar_letra(palabra, letra)}")

    elif opcion == "5":
        cadena = input("Ingrese una cadena de texto: ")

        print(f"Resultado: {invertir_cadena(cadena)}")

    elif opcion == "6":
        print()

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")
