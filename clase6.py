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