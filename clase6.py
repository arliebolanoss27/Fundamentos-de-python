'''
Clase:        6
Tema:         Aprendiendo con listas
Ejercicio:    Eliminando valores duplicados de una lista
Descripción:  Eliminar los numeros duplicados de una lista y mostrar la lista resultante.

Autor:        Arlette Bolaños
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

#Forma 1 de hacer el ejercicio con lo visto en clase
# Hacer la lista de numeros
lista = list(map(int, input().split(' ')))#Hay que saber que la entrada es una lista de numeros separados por espacios
# Eliminar los numeros duplicados
lista_sin_numeritos_repetidos = list(set(lista))
# Mostrar la lista resultante
print("Lista sin duplicaditos:", lista_sin_numeritos_repetidos)

#Forma 2 de hacer el ejercicio según repaso en refuerzo
lista2 = list(map(int, input().split(' ')))  # Entrada de lista de números, de la misma forma que antes
l = []
for i in lista2:
    if i not in l:  # Verificar si el número no está en la lista l
        l.append(i)  # Si no está, lo agregamos a la lista l.
print("Lista sin duplicaditos:", l)  # Mostrar la lista resultante sin duplicados

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