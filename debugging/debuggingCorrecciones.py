def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio: #Faltaban los 2 puntos
            print(f"{num} es mayor que el promedio.")
        elif num < promedio: #Faltaban los 2 puntos
            print(f"{num} es menor que el promedio.")
        else: #Faltaban los 2 puntos
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = float(input("Introduce un número: ")) #Faltaba especificar que la variable debian ser numeros, osea floats
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)