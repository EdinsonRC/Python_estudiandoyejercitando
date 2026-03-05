# ===================================================
# ? LECCIÓN 3: BUCLES (Loops)
# Automatizando Tareas Repetitivas
# los bucles permiten REPETIR código automáticamente
# Sin bucles tendrias que escribir lo mismo muchas veces
# ===================================================
# ! -------------------------------------------------
# 🎯 OBJETIVOS DE ESTA LECCIÓN:
# Entender cómo fucnionan los bucles for y while
# Iterar sobre secuencias(rangos,strings,listas)
# Usar break, continue y else en bucles
# Crear patrones, tablas y programas interactivos
# Evitar bucles infinitos
# !--------------------------------------------------

# * =================================================
# ! PARTE 1: BUCLE FOR - Repetir con Control
# Iterar un número especifico de veces
# * =================================================

# todo Sintaxis básica:
# ! for variable in secuencia:
# *    código que se repite

# todo ----------------------------------------------
# ? Ejemplo 1: Imprimir números del 1 al 5
# todo ----------------------------------------------

print('=== Ejemplo 1: Números del 1 al 5 ===')
for i in range(1,6):   # range(inicio, fin) - el fin NO se incluye
  # i es la variable que cambia en cada iteración
  # Primera vuelta: i = 1
  # Segunda vuelta: i = 2
  # Tercera vuelta: i = 3
  # Cuarta vuelta : i = 4
  # Quinta vuelta: i = 5
  print(f'Número: {i}')

# Sin bucle necesitarias escribir:
# print('Número: 1')
# print('Número: 2')
# print('Número: 3')
# print('Número: 4')
# print('Número: 5')

# ===================================================
# ! 2. LA FUNCIÓN range() - Generar secuencias
# ===================================================

# range() crea una secuencia de números

# --- range(fin) - desde 0 hasta fin-1 ---
print('\n=== range(5) - del 0 al 4 ===')
for i in range(5):   # 0, 1, 2, 3, 4
  print(i, end=' ')   # end=' ' imprime en la misma linea
print()   # Salto de linea al final

# --- range(inicio, fin) - desde inicio hasta fin-1 ---
print('\n=== range(1,6) - del 1 al 5 ===')
for i in range(1, 6):   # 1, 2, 3, 4, 5
  print(i,end=' ')
print()

# --- range(inicio, fin, paso) - con saltos ---
print('\n=== range(0, 11, 2) - números pares del 0 al 10 ===')
for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10
  print(i, end= ' ')
print()

# Números impares
print('\n=== range(1, 11, 2) - números impares del 1 al 10 ===')
for i in range(1, 11, 2):   # 1, 3, 5, 7, 9
  print(i,end=' ')
print()

# Cuenta regresiva(paso negativo)
print('\n=== range(10, 0, -1) - cuenta regresiva ===')
for i in range(10, 0, -1):   # 10, 9, 8, ...., 1
  print(i, end= ' ')
print()

# ===================================================
# ! 3. ITERAR SOBRE STRINGS (TEXTOS)
# ===================================================

# Puedes recorrer cada letra de un texto
print('\n=== Iterando sobre un string ===')
palabra = 'Python'

for letra in palabra:   # Recorre cada carácter
  print(f'Letra: {letra}')


# Ejemplo práctico: Contar vocales
print('\n=== Contador de vocales ===')
texto = 'Hola Mundo'
vocales = 'aeiouAEIOU'
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1  # Equivale a: contador = contador + 1
        print(f"✓ '{letra}' es vocal")

print(f'Total de vocales: {contador}')

# ===================================================
# ! 4. ACUMULADORES - Sumar valores en bucles
# ===================================================

# Un acumulador guarda valores que se van sumando

print('\n=== Suma de números del 1 al 10 ===')
suma_total = 0   # Acumulador inicializado en 0

for numero in range(1,11):
  suma_total += numero   # Suma_total = suma_total + numero
  print(f'Agregando {numero}, suma actual: {suma_total}')

print(f'Suma total: {suma_total}')   # 1+2+3+...+10 = 55

# ===================================================
# ! 5. BUCLES ANIDADOS -Un bucle dentro de otro
# ===================================================

# Útil para crear patrones, matrices, tablas

print('\n=== Tabla de multiplicar del 1 al 5 ===')
for i in range(1,6):   # Primer bucle: números de 1 al 5
  for j in range(1,11):   # Segundo bucle: multiplica del 1 al 10
    resultado = i * j
    print(f'{i} x {j} = {resultado}')
  print('-' * 20)   # Separador entre tablas

# Patrón de asteriscos
print('\n=== Patrón triangular ===')
for fila in range(1,6):   # 5 filas
    for columna in range(fila):   # columnas = número de fila
        print('*', end="")   # Imprime asterisco sin sato de linea
    print()   # Salto de linea al final de cada fila

# Resultado:
# *
# **
# ***
# ****
# *****

# ===================================================
# ! 6. BUCLE WHILE - Repetir mientras se cumpla una condición
# ===================================================

# Sintaxis:
# while condición:
#   código que se repite

# todo: El bucle se ejecuta MIENTRAS la condición sea True

print('\n=== Bucle while: Cuenta del 1 al 5 ===')
contador = 1   # Variable de control

while contador <= 5:   # Mientras contador sea menor o igual a 5
  print(f'Contador: {contador}')
  contador += 1   # IMPORTANTE: incrementar o el bucle será infinito
print('Bucle terminado')

# ===================================================
# ! 7. DIFERENCIA ENTRE FOR Y WHILE
# ===================================================

# FOR : Cuando sabes CUÁNTAS veces repetir
#       Ejemplo: 'Imprime los números del 1 al 10'

# WHILE : Cuando NO sabes cuántas veces, pero conoces la CONDICIÓN
#         Ejmplo: 'Pide números hasta que el usuario ingrese 0'

# ===================================================
# ! 8. BREAK - Salir del bucle inmediatamente
# ===================================================
print('\n=== uso de break ===')
for i in range(1, 11):
  if i == 5:
    print(f'¡Encontré el {i}! Saliendo del bucle')
    break   # Detiene el bucle completamente
  print(i)

print('Después del bucle')

# Ejemplo práctico: Buscar un número
print('\n=== Buscamos el número 7 ===')
numeros = [3, 7, 2, 9, 7, 1]

for numero in numeros:
    if numero == 7:
        print(f"✓ Encontré el 7 en la posición actual")
        break   # Sale del bucle cuando encuentra el primero
    print(f'Revisando: {numero}')

# ===================================================
# ! 9. CONTINUE - Saltar a la siguiente iteracción
# ===================================================

print('\n=== Uso de continue ===')
for i in range(1,11):
  if i % 2 == 0:   # Si es par
    continue   # Salta al siguiente número sin ejecutar lo de aabajo
  print(f'{i} es impar')   # Solo se ejecuta para impares

# todo Ejemplo: Imprimir solo números positivos
print('\n=== Solo números positivos ===')
numeros = [5, -3, 8, -1, 0, 12, -7]

for numero in numeros:
    if numero <= 0:   # Si es negativos o cero
        continue   # Salta este número
    print(numero)   # Solo imprime positivos

# ===================================================
# ! 10. ELSE EN BUCLES - Se ejecuta si el bucle termina normal
# ===================================================

# else en bucles se ejecuta si el bucle NO fue interrumpido con break

print('\n=== Bucle con else (sin break) ===')
for i in range(1,6):
    print(i)
else:
    print("✓ Bucle completado sin interrupciones")

print('\n=== Bucle con else (con break) ===')
for i in range(1,6):
    if i == 3:
        print('Interrumpiendo en 3')
        break
    print(i)
else:
    print("Este mensaje NO se muestra porque hubo break")

# ===================================================
# ! 11. VALIDACIÓN CON WHILE - Pedir datos hasta que sean correctos
# ===================================================

print('\n=== Validación de entrada ===')

# Pedir un número positivo
numero_valido = False   # Bandera (flag)

while not numero_valido:   # Mientras no se valido
    numero = int(input('Ingresa un número positivo: '))
    if numero > 0:
        print(f"✓ Gracias, ingresaste {numero}")
        numero_valido = True   # Cambia la bandera para salir del bucle
    else:
        print("❌ Error: El número debe ser positivo. Intenta de nuevo.")

# Método alternativo (más usado):
while True:   # Bucle infinito controlado
    edad = int(input("\n Ingresa tu edad (1 - 120): "))

    if 1 <= edad <= 120:
        print(f"✓ Edad valida: {edad}")
        break   # Sale del bucle si la edad es válida
    else:
        print("❌ Edad invalida. Debe estar entre 1 y 120.")

# ===================================================
# ! 12. ENUMERATE () - Obtener indice y valor
# ===================================================

print('\n=== Usando enumerate() ===')
frutas = ['manzana', 'banana', 'naranja', 'uva']

# sin enumerate (forma básica)
print('Sin enumerate: ')
for i in range(len(frutas)):   # len() devuelve el tamaño
  print(f'Posición {i}: {frutas[i]}')

# Con enumerate (forma profesional)
print('\nCon enumerate: ')
for indice, fruta in enumerate(frutas):
  print(f'Posición {indice}: {fruta}')

# Empezar desde 1 en lugar de 0
print('\nEnumerate desde 1: ')
for numero, fruta in enumerate(frutas, start=1):
    print(f'{numero}.{fruta}')

# ===================================================
# ! 13. LISTAS POR COMPRENSIÓN (List Comprehension)
# ===================================================

# Forma compacta de crear listas con bucles

# Forma tradicional: Números del 1 al 10
numeros = []
for i in range(1,11):
  numeros.append(i)   # append() agrega al final de la lista
print(f'\nForma tradicional: {numeros}')

# List comprehension (forma compacta):
numeros = [i for i in range(1,11)]
print(f'List comprehension: {numeros}')

# Crear lista de cuadrados
cuadrados = [x**2 for x in range(1,11)]
print(f'Cuadrados: {cuadrados}')   # [1, 4, 9, 16, 25, ...]

# on condición: Solo números pares
pares = [x for x in range(1,21) if x % 2 ==0]
print(f'Numeros pares: {pares}')   # [2, 4, 6, 8, 10, ...]

# ===================================================
# ! 14. EJEMPLO COMPLETO: Juego "ADIVINA EL NÚMERO"
# ===================================================

import random   # Módulo para generar números aleatorios

print('='*50)
print('"🎮" JUEGO: ADIVINA EL NÚMERO'.center(50))
print('='*50)

numero_secreto = random.randint(1, 100)   # Número aleatorio de 1 al 100
intentos = 0   # Contador de intentos
intentos_maximos = 3

print('Estoy pensando en un número entre 1 y 100')
print(f'Tienes {intentos_maximos} intentos para adivinar\n')

while intentos < intentos_maximos:
    intentos += 1
    print(f"Intento {intentos} / {intentos_maximos}")

    intento = int(input("¿Cuál es tu número? "))

    if intento == numero_secreto:
        print(f"\n🎉 ¡FELICITACIONES! Adivinaste en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El numero es MAYOR 📈")
    else:
        print("El número es MENOR 📉")
else:
    # Este else se ejecuta si el while termina sin break
    print(f"\n GAME OVER 💀. El número era {numero_secreto}".center(50))

# ===================================================
# ! 15. EVITAR BUCLES INFINITOS
# ===================================================

# ❌ BUCLE INFINITO - NUNCA HAGAS ESTO:
# while True:
#   print('Esto se repetirá para siempre)
#   # No hay break ni forma de salir

# ✅ BUCLE CONTROLADO:
contador = 0
while contador < 5:
    print(f'Vuelta {contador}')
    contador +=1   # CRÍTICO: incrementar el contador

# Tip: Si tu programa se queda "colgado", presiona Ctrl + C para detenerlo

# ===================================================
# * RESUMEN DE ESTA LECCIÓN
# ===================================================

print('='*50)
print('RESUMEN - LECCIÓN 3')
print('='*50)
print('1. for : Repetir un número especifico de veces')
print('2. range(): Generar secuencias de números')
print('3. while: Repetir mientras se cumpla una condición')
print('4. break: Salir del bucle inmediatamente')
print('5. continue: Saltar a la siguiente iteracción')
print('6. else en bucles: Se ejecuta si NO hubo break')
print('7. Bucles anidados: un bucle denro de otro')
print('8. enumerate(): Obtener indice y valor')
print('9. List comprehension: Crear listas compactas')
print('='*50)

# ===================================================
# * TABLA DE DIFERENCIAS: FOR VS WHILE
# ===================================================

print("\n📊 FOR vs WHILE: ")
print('-'*50)
print('FOR:')
print("✓ Sabes cuántas veces repetir")
print("✓ Iterar sobre secuencias (listas, strings, rangos)")
print("✓ Más común y seguro")
print('='*50)
print('\nWHILE:')
print("✓ No sabes cuántas veces, solo la condición")
print("✓ Validar datos del usuario")
print("✓ Cuidado con bucles infinitos")
print('-'*50)
