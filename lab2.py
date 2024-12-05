# Función para descomponer un número en factores primos
def descomponer_factores(numero):
    factores = []
    divisor = 2  # Comenzamos con el número primo más pequeño
    while numero > 1:
        if numero % divisor == 0:  # Si es divisible, lo agregamos
            factores.append(divisor)
            numero //= divisor  # Dividimos para seguir descomponiendo
        else:
            divisor += 1  # Si no es divisible, pasamos al siguiente número
    return factores


# Función para el MCD con descomposición factorial
def calcular_mcd_factores(numeros):
    factores_todos = [descomponer_factores(num) for num in numeros]
    comunes = set(factores_todos[0])
    for factores in factores_todos[1:]:
        comunes = comunes.intersection(factores)  # Encontramos los factores comunes
    mcd = 1
    for factor in comunes:
        # Contamos cuántas veces aparece el factor y tomamos el mínimo
        potencias = [factores.count(factor) for factores in factores_todos]
        mcd *= factor ** min(potencias)
    return mcd


# Función para el MCM con descomposición factorial
def calcular_mcm_factores(numeros):
    factores_todos = [descomponer_factores(num) for num in numeros]
    todos = set(factores_todos[0])
    for factores in factores_todos[1:]:
        todos = todos.union(factores)  # Tomamos todos los factores únicos
    mcm = 1
    for factor in todos:
        # Contamos cuántas veces aparece el factor y tomamos el máximo
        potencias = [factores.count(factor) for factores in factores_todos]
        mcm *= factor ** max(potencias)
    return mcm


# Función para el MCD con el algoritmo de Euclides
def calcular_mcd_euclides(numeros):
    def mcd(a, b):
        while b != 0:
            a, b = b, a % b  # Aquí hacemos el cálculo del residuo
        return a

    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mcd(resultado, num)  # Calculamos el MCD con cada número
    return resultado


# Función para el MCM con el algoritmo de Euclides
def calcular_mcm_euclides(numeros):
    def mcm(a, b):
        return a * b // calcular_mcd_euclides([a, b])  # Usamos la fórmula

    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mcm(resultado, num)  # Calculamos el MCM con cada número
    return resultado


# Aquí ponemos un menú para que el usuario elija
def mostrar_menu():
    print("¡Hola! Esto calcula el MCD y MCM de números.")
    print("1. Usar el método de descomposición factorial")
    print("2. Usar el método del algoritmo de Euclides")
    print("3. Salir")


# Aquí está el programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == "3":
            print("Adiós :)")
            break

        if opcion in {"1", "2"}:
            numeros = list(
                map(int, input("Escribe los números separados por espacio: ").split())
            )

            if opcion == "1":
                print("Con el método de descomposición factorial:")
                print("MCD:", calcular_mcd_factores(numeros))
                print("MCM:", calcular_mcm_factores(numeros))
            elif opcion == "2":
                print("Con el método del algoritmo de Euclides:")
                print("MCD:", calcular_mcd_euclides(numeros))
                print("MCM:", calcular_mcm_euclides(numeros))
        else:
            print("Esa no es una opción válida, intenta otra vez.")


# Aquí empieza el programa
if __name__ == "__main__":
    main()
