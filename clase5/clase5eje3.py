'''
Clase:        5
Tema:        Bloques iterativos
Ejercicio:    Sumador de valores posicionales
Descripción: Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito.
Autor:        Arlette Bolaños
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
#Ejercicio 3
numero = int(input("Ingrese un número: "))  # Pido al usuario que ingrese un número y lo guardo como una cadena de texto.
while numero>=10: #Esto quiere decir que este bucle se repite mientras el número tenga más de un dígito
    sumita=0 #Vamos a crear una variable sumita que va a almacenar la suma de los dígitos del número.
    # Recorremos cada dígito del número con un for para sumar sus valores.
    for di in str(numero):# Convertimos el número a cadena para poder iterar sobre sus dígitos.
        sumita = sumita + int(di)# Convertimos cada dígito de nuevo a entero y lo sumamos a sumita.
    print(f"{numero} = {sumita}")# Mostramos el número original y la suma de sus dígitos.
    numero = sumita #Finalmente, actualizamos el número y nos quedaría el resulado final.