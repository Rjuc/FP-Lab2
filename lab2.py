# Función para descomponer un número en sus factores primos básicos

def descomponer_factores(numero):
    factores = []
    divisor = 2  # Comenzamos con el número primo más pequeño, después del 1
    while numero > 1:
        if numero % divisor == 0:  # Si el número es divisible, se guarda el divisor en el arreglo "factores"
            factores.append(divisor)
            # Se divide el número por el divisor Para seguir buscando factores
            numero //= divisor
        else:
            # Pasamos al siguiente número
            divisor += 1  
    return factores

# MCD usando el método de descomposición factorial
def MCD_metodo1(numeros):
    # Obtenemos los factores de cada número en la lista "numeros" y los guardamos en "factores_todos"
    factores_todos = [descomponer_factores(num) for num in numeros]
    # Tomamos los factores comunes entre los números de la lista "numeros" y los guardamos en "comunes"
    comunes = set(factores_todos[0])
    # Iteramos sobre los factores de los números en "factores_todos" para encontrar los factores comunes
    for factores in factores_todos[1:]:
        comunes = comunes.intersection(factores)  # Tomamos los factores comunes 
    mcd = 1
    for factor in comunes:
        potencias = [factores.count(factor) for factores in factores_todos]
        mcd *= factor ** min(potencias)  # Usamos la potencia menor
    return mcd

def MCM_metodo1(numeros):
    factores_todos = [descomponer_factores(num) for num in numeros]
    todos = set(factores_todos[0])
    for factores in factores_todos[1:]:
        todos = todos.union(factores)  # Tomamos todos los factores
    mcm = 1
    for factor in todos:
        potencias = [factores.count(factor) for factores in factores_todos]
        mcm *= factor ** max(potencias)  # Usamos la potencia mayor
    return mcm

# MCD usando el algoritmo de Euclides
def MCD_metodo2(numeros):
    def mcd(a, b):
        while b != 0:  # Seguimos hasta que el residuo sea 0
            a, b = b, a % b
        return a
    
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mcd(resultado, num)  # Aplicamos el algoritmo iterativamente
    return resultado

# MCM usando el algoritmo de Euclides
def MCM_metodo2(numeros):
    def mcm(a, b):
        return a * b // MCD_metodo2([a, b])  # Fórmula para calcular el MCM
    
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mcm(resultado, num)  # Calculamos iterativamente
    return resultado

# Menú para que el usuario elija
def mostrar_menu():
    print("Programa para calcular MCD y MCM")
    print("1. Método de Descomposición Factorial")
    print("2. Método del Algoritmo de Euclides")
    print("3. Salir")

# Programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "3":
            print("¡Adiós!")
            break
        
        if opcion in {"1", "2"}:
            numeros = list(map(int, input("Escribe los números separados por espacio: ").split()))
            
            if opcion == "1":
                print("Usando el método de Descomposición Factorial:")
                print("MCD:", MCD_metodo1(numeros))
                print("MCM:", MCM_metodo1(numeros))
            elif opcion == "2":
                print("Usando el método del Algoritmo de Euclides:")
                print("MCD:", MCD_metodo2(numeros))
                print("MCM:", MCM_metodo2(numeros))
        else:
            print("Opción inválida, intenta otra vez.")

# Inicia el programa
if __name__ == "__main__":
    main()

