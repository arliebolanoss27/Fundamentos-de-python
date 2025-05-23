'''
Clase:        Variables, tipos, entradas y salidas
Tema:         Variables
Ejercicio:    Ejercicios con variables
Descripción:  Hacer un total de la cuenta con propina al usuario y Hacer una división con decimales y con presición.

Autor:        Arlette Bolaños
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

#Ejercicio 1
#Pedirle al usuario el total de una cuenta
#Porcentaje de propina
#Calcular el total a pagar

total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese propina: "))
propina = total_cuenta * (porcentaje_propina / 100)
total_a_pagar = total_cuenta + propina
print("El total de la cuenta es: ", total_cuenta)
print("La propina es: ", propina)
print("El total a pagar es: ", total_a_pagar,"con porcentaje de propina de: ", porcentaje_propina, "%")

#Ejercicio 2
a = int(input())   
b = int(input())  
k = int(input())   


resultado = str(a // b) + "."

resto = a % b
if resto < 0:
    resto = -resto
b = abs(b)

for i in range(k):
    resto *= 10
    digito = resto // b
    resultado += str(digito)
    resto = resto % b

print(resultado)
