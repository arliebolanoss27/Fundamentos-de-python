import numpy as np


my_list = [1, 2, 3, 4, 5]

arr = np.array(my_list)
print(arr)

#siguiente ejercicio
# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
print(result)

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 
# Recupera los elementos en los índices especificados: [1, 3, 5]
print(result)

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print(concatenated) 

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales
print(split)  

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])
print(consumo)

# Exploración inicial de los datos
print("Dimensiones:", consumo.ndim)               # 2 (filas y columnas)
print("Forma:", consumo.shape)                    # (10, 7) → 10 filas y 7 columnas
print("Tipo de datos:", consumo.dtype)            # float64 (números decimales)
print("Consumo primer hogar:", consumo[0])        # Todos los datos de la fila 0
print("Consumo el miércoles (día 3):", consumo[:, 2])  # Todos los datos de la columna 2

# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
minimos = np.min(consumo, axis=0)

# Desviación estándar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)

# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

# Índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100

# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con consumo mayor a 100: {consumo_mayor_100}")

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado
print(consumo_normalizado)

#Preguntas
#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo[4, 5]  # Resultado: 18.0
print(f"Consumo del hogar 5 el viernes: {consumo[4, 5]}")
#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
consumo[-3:, 6]  # Resultado: array([12. , 16.7,  9.3])
print(f"Consumo de los últimos 3 hogares el domingo: {consumo[-3:, 6]}")
#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
np.mean(consumo[:, 5:7])  # Resultado: 13.615
print(f"Promedio de consumo los fines de semana: {np.mean(consumo[:, 5:7])}")
#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
np.std(consumo, axis=0)  # Mayor valor en índice 5 (sábado)
print(f"Desviación estándar por día: {np.std(consumo, axis=0)}")
#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
np.argsort(np.sum(consumo, axis=1))[:3]
print(f"Índices de los 3 hogares con menor consumo total: {np.argsort(np.sum(consumo, axis=1))[:3]}")
#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
np.sum(consumo[2] * 1.10)
print(f"Nuevo consumo total semanal del hogar 3: {np.sum(consumo[2] * 1.10)}")