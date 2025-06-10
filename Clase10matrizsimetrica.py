#Ejercicio 2:
'''''
Clase:        10
Tema:         Matrices y listas
Ejercicio:    Matriz simetrica
Descripción:  Dada una matriz cuadrada ingresada por el usuario, comprueba si la matriz cuadrada es simétrica respecto a su diagonal principal.

Autor:        Arlette Bolaños
Fecha:        2025-06-10
Estado:       [   Terminado ]
'''

n =int(input())
m = []
for i in range(n):
    temp = list(map(int, input().split(',')))
    m.append(temp)
#Ahora vamos con el codigo para comprobar si la matriz es simetrica o no
simetrica = True
for i in range(n):
    for j in range(i + 1, n):  # Solo compara la mitad superior con la inferior
        if m[i][j] != m[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")