
#* Ejercicio 1: Suma de números pares en una lista
#* Descripción: Escribe una función que reciba una lista de números y 
#* devuelva la suma de todos los números pares.
#suma_pares([1, 2, 3, 4, 5, 6])  # Debe retornar 12 (2 + 4 + 6)
lista = [1,2,3,4,5,6]

def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)
resultado = suma_pares(lista)
print(f"la suma de los pares es : {resultado}") #12
            
#* Ejercicio 2: Contar vocales en una cadena
#* Descripción: Crea una función que cuente cuántas vocales (a, e, i, o, u) hay en una cadena.   
cadena = "Hola Mundo"# Debe retornar 4 (o, a, u, o)
def contar_vocal(cadena):
    return sum(1 for letra in cadena if letra.lower() in "aeiou")
print(contar_vocal(cadena))

#* Ejercicio 3: Encontrar el número más grande en una lista
#*Descripción: Implementa una función que encuentre el número más 
#* grande en una lista (sin usar max()).
maximo =[3, 8, 12, 10, 5]  # Debe retornar 10
def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo
resultado = encontrar_maximo(maximo)
print(f"el maximo numero es: {resultado}")   

