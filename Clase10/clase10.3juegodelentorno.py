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

n = int(input())
m = int(input())

datos = []
for i in range(n):
    datos.append(list(map(int, input().split(','))))

res = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x < n and 0 <= y < m and not (x == i and y == j):
                    res[i][j] += datos[x][y]

for fila in res:
    print(fila)
