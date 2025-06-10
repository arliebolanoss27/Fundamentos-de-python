'''
Clase:        6
Tema:         Números líderes
Ejercicio:    Imprimir todos los valores líderes de una lista
Descripción:  Imprimir todos los números líderes en una lista. Un número es líder si es mayor que todos los números a su derecha.

Autor:        Arlette Bolaños
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

#Ejercicio 2
# Hacer la lista de numeros
lista3 = list(map(int, input().split(' ')))  # Entrada de lista de números, de la misma forma que antes
# Encontrar los números líderes
lideres = []  # Lista para almacenar los números líderes
for i in range(len(lista3) - 1): # Recorremos la lista hasta el penúltimo elemento
    # Verificamos si el número en la posición i es líder
    es_lider = True
    for j in range(i + 1, len(lista3)): # Recorremos los números a la derecha del número en la posición i
        if lista3[i] <= lista3[j]: # Si el número en la posición i es menor o igual a alguno de los números a su derecha
            es_lider = False # Entonces no es líder
            break
    if es_lider:
        lideres.append(lista3[i])# # Si es líder, lo agregamos a la lista de líderes
print(' '.join(map(str, lideres)))# Y por último, ya imprimimos los números líderes por separado jeje.