# ===========================================
# ? LECCIÓN 01: VARIABLES Y TIPOD DE DATOS
# ===========================================

# La función print() muestra texto en la consola/terminal
# todo lo que está entre comillas se imprime exactamente como está.
print("¡Bienvenido a Python!")  # Este es un comentario en linea

# =============================================
# ? 1. VARIABLES: Cajas que guardan información
# =============================================

# Una variable es como una caja con una etiqueta
# nombre_variable = valor_que_guardas

nombre = "Carlos"  # Variable tipo texto (String o str)
# "nombre" es la etiqueta de la caja
# "Carlos" es lo que guardamos dentro
# " El simbolo = significa "asignar" (no es igualdad matemática)

# Imprimimos el contenido de la variable
print(nombre)  # Muestra: Carlos

# Podemos cambiar el valor de una variable en cualquier momento
nombre = "Maria"  # Ahora la caja "nombre" contiene "Maria"
print(nombre)  # Muestra: Maria

# ======================================================
# ? 2. TIPOS DE DATOS BÁSICOS
# ======================================================

# --- NÚMEROS ENTEROS (int = integer) ---
edad = 25  # Un número sin decimales
print(edad)  # Muestra: 25

# Podemos hacer operaciones matmáticas
edad = edad + 1  # Sumamos 1 a la edad
print(edad)  # Muestra: 26

# --- NÚMEROS DECIMALES (float = punto flotante) ---
altura = 1.75  # Números con decimales usan punto (.) no coma
peso = 70.5
print(altura)  # Muestra: 1.75

# --- TEXTOS / CADENAS (str = string) ---
apellido = "Garcia"  # Texto entre comillas simples
ciudad = "Lima"  # También puede usar comillas dobles

#! Concatenación: unir textos con el simbolo +
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Muestra: María Garcia

# --- BOOLEANOS (bool = boolean) ---
# Solo pueden ser True (verdadero) o False (falso)
# Nota: En Python se escriben con mayúscula inicial
es_estudiante = True  # Verdadero
tiene_trabajo = False  # Falso
print(es_estudiante)  # Muestra: True

# ======================================================
# ? 3. LA FUNCIÓN Type() - Verificar tipos
# ======================================================

# type() nos dice que tipo de dato es una variable
print(type(edad))  # Muestra: <class 'int'>
print(type(altura))  # Muestra: <class 'float'>
print(type(nombre))  # Muestra: <class 'str'>
print(type(es_estudiante))  # Muestra: <class 'bool'>

# ========================================================
# ? 4. IMPRIMIENDO CON FORMATO
# ========================================================

# Método antiguo: concatenación
print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años")
# Nota: str(edad) convierte el número a texto para poder concatenar

# Método moderno: f-strings (recomendado)
# Colocamos f antes de las comillas y usamos {} para variables
print(f"Mi nombre es {nombre} y tengo {edad} años")
# Esto es más fácil de leer y escribir

# Puedes incluir operaciones dentro de {}
print(f"El año que viene tendré {edad + 1} años")

# ==========================================================
# ? 5. NOMBRES DE VARIABLES - REGLAS IMPORTANTES
# ==========================================================
#! CORRECTO ✅
mi_nombre = "Edinson"  # snake_case (recomendado en Python)
miNombre = "Edinson"  # camelCase (tambien valido)
nombre2 = "Edinson"  # Puede incluir números (pero no al inicio)
_nombre = "Edinson"  # Puede empezar con guión bajo

#! INCORRECTO ❌
# 2nombre = "Juan"    # No puede empezar con número
# mi-nombre = "Juan"  # No puede usar guiones (-)
# mi nombre = "Juan"  # No puede tener espacios
# class = "Juan"      # No puede usar palabras reservadas de python

# * 💡 BUENAS PRÁCTICAS:
# - Usa nombres descriptivos: "edad" es mejor que "e"
# - Usa minúsculas con guiones bajos: "nombre_completo"
# - Evita nombres de una sola letra (excepto en bucles)

# ==========================================================
# ? 6. ENTRADA DE DATOS - input()
# ==========================================================
# input() permite que el usuario escriba algo
# Siempre devuelve texto (string), incluso si escribes números

print("\n--- SECCIÓN INTERACTIVA ---")
tu_nombre = input("¿Cuál es tu nombre? ")  # Espera que escribas
print(f"¡Hola, {tu_nombre}!")

# Si necesitas un número, debes convertirlo
tu_edad = input("¿Cuántos años tienes? ")  # Esto es texto
tu_edad = int(tu_edad)  # Convertimos texto a número entero
print(f"Tienes {tu_edad} años")

# También puedes convertir y guardar en una sola linea

tu_altura = float(input("¿Cuánto mides en metros?"))  # float para decimales
print(f"Mides {tu_altura} metros")

# =============================================================
# ? 7. OPERACIONES BÁSICAS
# =============================================================

# Aritméticas
a = 10
b = 3

suma = a + b  # Resultado 13
resta = a - b  # Resultado 7
multiplicacion = a * b  # Resultado 30
division = a / b  # 3.333... (siempre devuelve float)
division_entera = a // b  # 3 (solo la parte entera)
modulo = a % b  # 1 (El residuo de la división)
potencia = a**b  # 1000 (10 elevado a la 3)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Modulo: {modulo}")
print(f"potencia: {potencia}")

# ================================================================
# ? 8. CONVERSIONES DE TIPO (Type Casting)
# ================================================================

# A veces necesitas convertir entre tipos de datos

numero_texto = "100"  # Esto es texto
numero_real = int(numero_texto)  # Convertimos a entero
print(f"Tipo antes: {type(numero_texto)}")  # <class 'str'>
print(f"Tipo después: {type(numero_real)}")  # <class 'int'>

# Otras conversiones comunes:
decimal_texto = "3.14"
decimal_numero = float(decimal_texto)  # str a float

numero = 42
numero_en_texto = str(numero)  # int a str

# ==================================================================
# ? 9. CONSTANTES (por convención)
# ==================================================================

# En Python no hay constantes "reales", pero por convecion
# usamos MAYÚSCULAS para indicar que no deben cambiar

PI = 3.14159  # Por convención, no cambies este valor
GRAVEDAD = 9.8
NOMBRE_EMPRESA = "TechCorp"

# Puedes cambiarlos técnicamente, pero NO deberias
# Es una regla de buenas prácticas

radio = 5
area_circulo = PI * (radio**2)
print(f"El área del circulo es: {area_circulo}")

#! ==================================================================
# ? RESUMEN DE ESTA LECCIÓN
#! ==================================================================

print("\n --- RESUMEN --- ")
print("1. Variables = caja que guardan datos")
print("2. Tipos: int, float, str, bool")
print("3. print() = mostrar en pantalla")
print("4. input() = recibir datos del usuario")
print("5. f-strings = formato moderno para imprimir")
print("6. Operadores: +, -, *, /, //, %, **")
