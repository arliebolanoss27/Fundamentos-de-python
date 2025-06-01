'''
Clase:        5
Tema:        Bloques iterativos
Ejercicio:    Suma de valores
Descripción: Dada una lista de longitud variable de números enteros ingresada por el usuario,
calcula e imprime la suma de todos los números usando un bucle for.
Autor:        Arlette Bolaños
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lista_numeritos = list(map(int,input("Ingrese una lista de números enteros separados por espacios: ").split(' ')))
# Ya creamos la lista.
# Ejercicio 1
suma_total = 0
for numero in lista_numeritos:
    suma_total += numero# Es como lo mismo que decir suma_total = suma_total + numero
# Recorremos cada número en la lista y lo sumamos a la variable suma_total
print("La suma total de los números es:", suma_total)

'''
Clase:        5
Tema:        Bloques iterativos
Ejercicio:    ¡Adivina el número!
Descripción: Generar un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado. 
Autor:        Arlette Bolaños
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

#Ejercicio 2(con explicaciones de que voy haciendo paso a paso)
import random #En este caso es necesario importar la librería random para generar números aleatorios
numerito_secretojiji = random.randint(1, 100)#Esta función genera un número entero aleatorio entre 1 y 100, guardandolo en la variable.
print("¡Bienvenido al juego de adivinar el número en el codigo de Arlette!")
adivinado = False #Esta variable se usa para controlar el bucle, si es True, el bucle termina.
#Ahorita es false porque el usuario no ha adivinado el número
while not adivinado: #Inicié un bucle indefinido que se repetirá mientras el número no haya sido adivinado.
    #El bucle se va a romper cuando adivinado se vuelva True.
    intentito = int(input("Adivina el número entre 1 y 100: ")) #Pido al usuario que ingrese un número, lo convierto a entero y lo guardo en intentito.
    if intentito < numerito_secretojiji: #Si el número ingresado es menor que el númerito secreto...
        print("El número secreto es mayor que: ", intentito) #Le digo al usuario que el número secreto es mayor.
    elif intentito > numerito_secretojiji: #Si el número ingresado es mayor que el númerito secreto...
        print("El número secreto es menor que: ", intentito) #Le digo al usuario que el número secreto es menor.
    else: #Si no se cumple ninguna de las condiciones anteriores, significa que el usuario ha adivinado el número.
        print("¡Felicidades! Has adivinado el númerito secreto el cual era:", numerito_secretojiji) #Le doy la felicitación al usuario.
        print("Gracias por jugar al juego de adivinar el número en el codigo de Arlette, espero tengas lindo día :)") #Le doy las gracias al usuario por jugar jeje.	
        adivinado = True #Cambio la variable adivinado a True y eso hace que se rompa el bucle.

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