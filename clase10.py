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

# Ejercicio 3:
'''''
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