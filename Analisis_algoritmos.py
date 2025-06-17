# Importamos las librerias Time y Random Necesarias para hacer las pruebas
import time
import random

# Algoritmos de ordenamiento:
 
#1: Ordenamiento de Burbuja: obtenido de los apuntes de la materia unidad "Búsqueda y Ordenamiento"
def ordenamiento_burbuja(arr):
    n = len(arr)           # 1
    for i in range(n):     
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#2: Ordenamiento por insersion: obtenido de los apuntes de la materia unidad "Búsqueda y Ordenamiento"
def ordenamiento_insersion(arr):
    for i in range(1, len(arr)): #operacion i veces
        key = arr[i]  #1 operacion
        j = i - 1     #2 operacion
        while j >= 0 and key < arr[j]: #operacion j veces
            arr[j + 1] = arr[j] # 2
            j -= 1 
        arr[j + 1] = key #2 operaciones
    return arr
## T(n) = 1+(1+2+1*i)*(2+2*j)+1 = (5n*4n)+2 

#3: Ordenamiento por seleccion: obtenido de los apuntes de la materia unidad "Búsqueda y Ordenamiento"
def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_index = i # Encontrar el índice del elemento mínimo
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # Intercambiar el elemento mínimo con el elemento actual

#4: Quick Sort: obtenido de los apuntes de la materia unidad "Búsqueda y Ordenamiento"
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Medición de tiempos con la función time() de la libreria time
def medir_tiempo(func, lista):
    inicio = time.time()
    func(lista[:])
    fin = time.time()
    return fin - inicio

# Generación de listas aleatorias con la funcion random() de la libreria que importamos
listas = {
    'Pequeña (100)': random.sample(range(1000), 100),
    'Mediana (1.000)': random.sample(range(10000), 1000),
    'Grande (10.000)': random.sample(range(100000), 10000)
}
#Creamos un array con las funciones de ordenamiento que creamos anteriormente:
algoritmos = [ordenamiento_burbuja, ordenamiento_insersion, ordenamiento_seleccion, quick_sort]

for nombre, lista in listas.items():
    print(f"\nLista: {nombre}")
    for algoritmo in algoritmos:
        tiempo = medir_tiempo(algoritmo, lista)
        print(f"{algoritmo.__name__}: {tiempo:.6f} segundos")

