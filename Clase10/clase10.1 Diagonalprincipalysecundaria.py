'''''
Clase:        10
Tema:         Matrices y listas
Ejercicio:    Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el usario, crear dos listas:
              una con los elementos de la diagonal principal y otra con los de la diagonal secundaria.
              Imprimir ambas listas.

Autor:        Arlette Bolaños
Fecha:        2025-06-09
Estado:       [   Terminado ]
'''
#primero mirams de que tamaño es la matriz
n=int(input())
m=[]
for i in range(n):
    temp=list(map(int, input().split(',')))
    m.append(temp)

#creamos las dos listas
diagonal_principal = []
diagonal_secundaria = []
for i in range(n):
    diagonal_principal.append(m[i][i])  
    diagonal_secundaria.append(m[i][n - 1 - i]) 
print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)

# Ejercicio 3:
'''
Clase:        10
Tema:         Matrices y listas
Ejercicio:    Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el usuario, verifica para cada celda de una matriz binaria cuántos elementos con valor 
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).

Autor:        Arlette Bolaños
Fecha:        2025-06-09
Estado:       [   En progreso ]
'''