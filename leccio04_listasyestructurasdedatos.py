# ===================================================
# ? LECCION 4: Listas y Estructuras de Datos
# ===================================================
# ! -------------------------------------------------
# 🎯 OBJETIVOS DE ESTA LECCIÓN:
# - Crear y manipular listas en Python
# - Usar métodos de listas(append, remove, sort, etc)
# - Acceder a elementos con indices y slicing
# - Entender diccionarios, tuplas y sets
# - Trabajar con estructuras de datos anidadas
# !--------------------------------------------------

# * =================================================
# ! PARTE 1: LISTAS - La Estructura más importante
# - Una lista es una colección ORDENADA Y MODIFICABLE de elementos
# - Puede contener diferentes tipos de datos
# - Se define con corchetes []
# * =================================================

# ? =================================================
# ! 1. CREAR LISTAS
# ? =================================================

#  Lista vacia  =====================================
lista_vacia = []
print(f"Lista vacia: {lista_vacia}")
#  ==================================================

# ! Lista de números  ===============================
numeros = [1, 2, 3, 4, 5]
print(f"Números {numeros}")
# ===================================================

# * Lista de Strings  ===============================
frutas = ["manzana", "banana", "naranja", "uva"]
print(f"Frutas: {frutas}")
# ==================================================

# ? Listas mixtas (diferentes tipos)
mixta = [1, "hola", 3.14, True, [1, 2, 3]]
print(f"Lista mixta: {mixta}")
# ==================================================

# ! Crear lista con range()  =======================
numeros_range = list(range(1, 11))  # Convierte range a lista
print(f"Del 1 al 10: {numeros_range}")
# ==================================================

# ? =================================================
# ! 2. ACCEDER A ELEMENTOS - INDICES
# ? =================================================
# Los indices empiezan en 0 (primer elemento)
frutas = ["manzana", "banana", "naranja", "uva", "pera"]

print("\n=== Acceso por indice ===")
print(f"Primer elemento (indice 0): {frutas[0]}")  # manzana
print(f"Segundo elemento (indice 1): {frutas[1]}")  # banana
print(f"Tercer elemento (indice 2): {frutas[2]}")  # naranja

# Indices negativos (desde el final)
print(f"Último elemento (-1): {frutas[-1]}")  # pera
print(f"Penúltimo elemento (-2): {frutas[-2]}")  # uva
print(f"Antepenúltimo elemento (-3): {frutas[-3]}")  # naranja

# ? =================================================
# ! 3. MODIFICAR ELEMENTOS
# ? =================================================

print("\n=== Modificar elementos ===")
frutas = ["manzana", "banana", "naranja"]
print(f"Lista original: {frutas}")

# Cambiar un elemento
frutas[1] = "fresa"  # Cambia "banana" por "fresa"
print(f"Después de cambiar indice 1: {frutas}")

# Cambiar el último
frutas[-1] = "kiwi"
print(f"Después de cambiar el último: {frutas}")  # Cambia "naranja" por "kiwi"

# ? =================================================
# ! 4. MÉTODOS DE LISTAS - AGREGAR ELEMENTOS
# ? =================================================

print("\n=== Agregar elementos ===")
tareas = ["estudiar", "cocinar"]
print(f"Lista inicial: {tareas}")

# Metodos:
# Metodo append() - Agrega al final
tareas.append("hacer ejercicio")
print(f"Después de append: {tareas}")  # Agrega "hacer ejercicio" al final de la lista

# Metodo insert() - Inserta en una posición especifica
tareas.insert(1, "leer")  # Inserta en el indice 1
print(f"Después de insert en posición 1: {tareas}")
# Resultado: ['esudiar', 'leer', 'cocinar','hacer ejercicio']

# Metodo extend() - Agrega múltiples elementos de otra lista
mas_tareas = ["limpiar", "dormir"]
tareas.extend(mas_tareas)  # Agrega todos los elementos
print(f"Después de extend: {tareas}")

# Diferencia entre append y extend
lista1 = [1, 2, 3]
lista1.append([4, 5])  # Agrega la lista como UN elemento
print(f"Con append [4, 5]: {lista1}")  # [1, 2, 3, [4, 5]]

lista2 = [1, 2, 3]
lista2.extend([4, 5])  # Agrega cada elemento individual
print(f"Con extend [4, 5]: {lista2}")  # [1, 2, 3, 4, 5]

# ? =================================================
# ! 5. MÉTODOS DE LISTAS -ELIMINAR ELEMENTOS
# ? =================================================

print("\n=== Eliminar elementos ===")
numeros = [10, 20, 30, 40, 50]

# remove() - Elimina la PRIMERA ocurrencia del valor
numeros.remove(30)  # Busca y elimina el 30
print(f"Después de remove(30): {numeros}")

# pop() - Elimina y RETORNA el elemento de un indice
numero_eliminado = numeros.pop(1)  # Elimina el indice 1
print(f"Elemento eliminado con pop(1): {numero_eliminado}")
print(f"Lista después de pop: {numeros}")

# del - Elimina por indice (no retorna el valor)
colores = ["rojo", "verde", "azul", "amarillo"]
del colores[1]  # Elimina "verde"
print(f"Después de del colores[1]: {colores}")

# clear() - Vacia toda la lista
colores.clear()
print(f"Después de clear(): {colores}")  # []

# ? =================================================
# ! 6. MÉTODOS DE BÚSQUEDA Y CONTEO
# ? =================================================

print("\n=== Búsqueda y conteo ===")
numeros = [5, 2, 8, 2, 9, 2, 4]

# index() - Retorna el indice de la primera ocurrencia
indice = numeros.index(8)
print(f"El número 8 está en el índice: {indice}")

# count() - Cuenta cuantas veces aparece un elemento
cantidad = numeros.count(2)
print(f"El número 2 aparece {cantidad} veces")

# in - Verifica si un elemento existe (retorna True / False)
print(f"¿Está el 9 en la lista? {9 in numeros}")  # True
print(f"¿Está el 100 en la lista? {100 in numeros}")  # False

# ? =================================================
# ! 7. ORDENAR LISTAS
# ? =================================================

print("\n=== Ordenar listas ===")
numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {numeros}")

# sort() - Ordena la lista EN EL LUGAR (la modifica)
numeros.sort()  # Ascendente de menor a mayor
print(f"Después de sort(): {numeros}")

# sort(reverse=True) - Orden descendente
numeros.sort(reverse=True)
print(f"Orden descendente: {numeros}")

# sorted() - Retorna una NUEVA lista ordenada (no modifica la original)
numeros_originales = [5, 2, 8, 1, 9]
numeros_ordenados = sorted(numeros_originales)
print(f"Original (sin cambios): {numeros_originales}")
print(f"Nueva lista ordenada: {numeros_ordenados}")

# Ordenar strings (alfabéticamente)
nombres = ["Carlos", "Ana", "Beatriz", "David"]
nombres.sort()
print(f"Nombres ordenados: {nombres}")

# reverse() - Invierte el orden (no ordena, solo invierte)
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(f"Lista invertida: {numeros}")  # [5, 4, 3, 2, 1]

# ? =================================================
# ! 8. SLICING - REBANAR LISTAS
# ? =================================================

# Sintaxis: lista[inicio:fin:paso]
# inicio: indice donde empieza (incluido)
# fin: indice donde termina (NO incluido)
# paso: de cuánto en cuánto

print("\n === Slicing ===")
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Primeros 5 elementos
print(f"Primeros 5: {numeros[0:5]}")  # [0, 1, 2, 3, 4]
print(f"Primeros 5 (forma corta): {numeros[:5]}")  # [0, 1, 2, 3, 4]

# Desde el índice 5 hasta el final
print(f"Desde 5 al final: {numeros[5:]}")  # [5, 6, 7, 8, 9]

# Del indice 2 al 7
print(f"Del 2 al 7: {numeros[2:8]}")  # [2, 3, 4, 5, 6, 7]

# Últimos 3 elementos
print(f"Últimos 3: {numeros[-3:]}")  # [7, 8, 9]

# Con paso: cada 2 elementos
print(f"Cada 2 elementos: {numeros[::2]}")  # [0, 2, 4, 6, 8]

# Invertir lista con slicing
print(f"Lista invertida: {numeros[::-1]}")  # [9, 8, 7, ..., 0]

# ? =================================================
# ! 9. FUNCIONES ÚTILES CON LISTAS
# ? =================================================

print("\n=== Funciones con listas ===")
numeros = [10, 45, 23, 67, 12, 89, 34]

# len() - Longitud de la lista
print(f"Cantidad de elementos: {len(numeros)}")  # 7

# sum() - Suma de todos los elementos (solo números)
print(f"Suma total: {sum(numeros)}")  # 280

# max() - Valor máximo
print(f"Valor máximo: {max(numeros)}")  # 89

# min() - Valor minimo
print(f"Valor mínimo: {min(numeros)}")  # 10

# Calcular promedio
promedio = sum(numeros) / len(numeros)
print(f"Promedio: {promedio:.2f}")  # 40.00

# ? =================================================
# ! 10. COPIAR LISTAS
# ? =================================================

print("\n=== Copiar listas ===")

# ❌ INCORRECTO - Esto NO copia, solo crea una referencia
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 apunta a la MISMA lista
lista2.append(4)
print(f"lista1: {lista1}")  # [1, 2, 3, 4] ¡Se modifico!
print(f"lista2: {lista2}")  # [1, 2, 3, 4]

# ✅ CORRECTO - Formas de copiar
original = [1, 2, 3]

# Método 1: ccopy()
copia1 = original.copy()
copia1.append(4)
print(f"Original: {original}")  # [1, 2, 3] (sin cambios)
print(f"Copia: {copia1}")  # [1, 2, 3, 4]

# Método 2: list()
copia2 = list(original)

# Método 3: slicing
copia3 = original[:]

# ? =================================================
# ! 11. LISTAS ANIDADAS (LISTAS DENTRO DE LISTAS)
# ? =================================================

print("\n=== Listas anidadas ===")

# Matriz 3x3
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accede a elementos
print(f"Matriz completa:\n{matriz}")
print(f"Primera fila: {matriz[0]}")  # [1, 2, 3]
print(f"Elemento [1][2]: {matriz[1][2]}")  # 6

# Iterar sobre matriz
print("Recorriendo la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
        print()  # Salto de linea

# Lista de estudiantes con sus notas
estudiantes = [["Ana", 85, 90, 78], ["Carlos", 92, 88, 95], ["Beatriz", 78, 85, 82]]

# Mostrar información
for estudiante in estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1:]  # Todas menos el nombre
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Promedio = {promedio:.1f}")

# ? =================================================
# ! 12. LIST COMPREHENSION - Crear listas de forma compacta
# ? =================================================

print("\n=== List Comprehension ===")

# Forma tradicional: Cuadrados del 1 al 10
cuadrados = []
for i in range(1, 11):
    cuadrados.append(i**2)
    print(f"Cuadrados (tradicional): {cuadrados}")

    # List comprehension (forma compacta)
    cuadrados = [i**2 for i in range(1, 11)]
    print(f"Cuadrados (comprehension): {cuadrados}")

# Con condición: Solo números pares
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Números pares: {pares}")

# Transformar strings
nombres = ["Ana", "Carlos", "Beatriz"]
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(f"Nombres en mayusculas: {nombres_mayusculas}")

# ? =================================================
# ! 13. ENUMERAR LISTAS - ENUMERATE()
# ? =================================================

print("\n=== enumerate() ===")
frutas = ["manzana", "banana", "naranja", "uva"]

# Con enumerate obtienes indice y valor
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Empezar desde 1
print("\nDesde 1:")
for numero, fruta in enumerate(frutas, start=1):
    print(f"{numero}. {fruta}")

# ? =================================================
# ! 14. UNIR LISTAS CON OPERADORES
# ? =================================================

print('\n=== Operadores con Listas ===')

# Concatenar con +
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_combinada = lista1 + lista2
print(f'Concatenación: {lista_combinada}')

# Repetir con *
repetida = [1, 2] * 3
print(f'Repetición: {repetida}')     # [1, 2, 1, 2, 1, 2]

# ? =================================================
# ! 15. CONVERTIR ENTRE TIPOS
# ? =================================================

print('\n=== Conversiones ===')

# String a lista de caracteres
palabra = 'Python'
letras = list(palabra)
print(f'String a lista: {letras}')     # ['P', 'y', 't', 'h', 'o', 'n']

# Lista a String
lista_letras = ['H', 'o', 'l', 'a']
palabra = ''.join(lista_letras)     # join() une elementos
print(f'Lista a string: {palabra}')     # Hola

# Con separador
numeros_texto = ['1', '2', '3']
resultado = "-".join(numeros_texto)  # join() une elementos por guiones
print(f'Con separador: {resultado}')     # "1-2-3"

# Split - String a lista
frase = 'Hola mundo desde Python'
palabras = frase.split()     # split() Divide por espacios cada palabra
print(f'Split: {palabras}')     # ['Hola', 'mundo', 'desde', 'Python']

frase_csv = 'manzana, banana, naranja'
frutas = frase_csv.split(',')     # Divide por comas cada palabra
print(f"Split por coma: {frutas}")  # ['manzana', ' banana', ' naranja']
