'''
Clase:        2
Tema:         Bloque condicional
Ejercicio:    Ejercicios de contraseña segura y calculo de impuesto
Descripción:  Verificar si una contraseña es segura y calcular el impuesto a pagar por un producto.

Autor:        Arlette Bolaños
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
#Ejercicio 1
#Cadena de texto que represente una contraseña
#tiene que tener al menos 8 caracteres
#tiene que tener al menos una letra mayúscula
#tiene que tener al menos un número

contraseña = input("Introduce una contraseña: ")
mayuscula = False
numero=False
#for recorre cada letra de la contraseña
for i in contraseña:
    if i.isupper():
        mayuscula=True
    if i.isdigit():
        numero=True
if mayuscula ==True and numero==True and len(contraseña)>=8:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")
#Ejercicio 2
unidades = int(input())

if unidades <= 100:
    impuesto = 0
elif unidades <= 200:
    impuesto = (unidades - 100) * 0.5
else:
    impuesto = (100 * 0.5) + ((unidades - 200) * 0.7)

print("Impuesto aplicado: " + str(impuesto),"dolares")
