'''
Clase:        5
Tema:        Bloques iterativos
Ejercicio:    Suma de valores
Descripción: Dada una lista de longitud variable de números enteros ingresada por el usuario,
calcula e imprime la suma de todos los números usando un bucle for.
Autor:        Arlette Bolaños
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lista_numeritos = list(map(int,input("Ingrese una lista de números enteros separados por espacios: ").split(' ')))
# Ya creamos la lista.
# Ejercicio 1
suma_total = 0
for numero in lista_numeritos:
    suma_total += numero# Es como lo mismo que decir suma_total = suma_total + numero
# Recorremos cada número en la lista y lo sumamos a la variable suma_total
print("La suma total de los números es:", suma_total)
