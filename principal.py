def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

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
        num = 0

        while True:
            try:
                num = int(input("Ingrese un número entero positivo para calcular su factorial: "))
                if num >= 0:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")

        factorial = factorial(num)

    if opcion == "2":
        num = 0