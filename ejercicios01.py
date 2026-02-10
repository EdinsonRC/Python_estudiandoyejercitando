#! =====================================================
# ? EJERCICIO PRÁCTICOS
#! =====================================================

# * EJERCICIO 1: CALCULADORA DE EDAD:
# 1. Pide al usuario su año de nacimiento
# 2. Calcula su edad actual (año 2026)
# 3. Muestra el resultado con un mensaje bonito

#! Tu código aqui: aqui iniciamos a codear

print("=" * 50)  # Imprime el signo "=" 50 veces para decoración
print(
    "Bienvenido a la calculadora de edad".center(50)
)  # Imprime el titulo y el ".center(50)" es para centrar entre los 50 caracteres "="
print("=" * 50)  # Imprime el signo "=" 50 veces para decoración

nombre_usuario = input("¿Cuál es tu nombre?\n")  # Solicita ingresar nombre
print(
    f"Hola {nombre_usuario}, bienvenido a esta calculadora de edad"
)  # Imprime lo solicitado con f-strings

fecha_nacimiento = int(
    input("¿Cuál es el año de tú nacimiento?\n")
)  # Solicita ingresar año de nacimiento

ANO_ACTUAL = 2026  # Es una constante y siempre se usa en MAYÚSCULAS
resultado = (
    ANO_ACTUAL - fecha_nacimiento
)  # La variable "resultado" realiza la operación

print(f"{nombre_usuario}, tu edad es de {resultado} años")

#! ================================================================================================================

# * EJERCICIO 2: CONVERSOR DE TEMPERATURA:
# 1. Pide al usuario una temperatura en Celsius
# 2. Conviertela a Fahrenheit usando la fórmula: F = C * 9/5 + 32
# 3. Muestra ambas temperaturas con formato

#! Tu código aqui: aqui iniciamos a codear

print("*" * 50)
print("Bienvenido al conversor de temperatura".center(50))
print("*" * 50)

celsius = int(input("Ingresa la temperatura en grados Celsius\n"))

conversion_fahrenheit = float(celsius * 9 / 5 + 32)

print(
    f"Ingresaste la siguiente temperatura en Celsius: {celsius} y se convirtio a Fahrenheit: {conversion_fahrenheit}"
)

#! ================================================================================================================

# * EJERCICIO 3: CALCULADORA DE IMC:
# 1. Pide al usuario su peso en kg y su altura en metros.
# 2. Calcula el IMC usando: IMC 0 peso / (altura ** 2).
# 3. Muestra el resultado redondeado a 2 decimales.

#! Tu código aqui: aqui iniciamos a codear

print("-" * 50)
print("Bienvenido a la calculadora de IMC".center(50))
print("-" * 50)

peso = float(input("Ingresa tu peso en Kg:\n"))
altura = float(input("Ingrese su altura en metros:\n"))

IMC = peso / (altura**2)

print(
    f"Tu IMC es : {round(IMC,2)}"
)  # {round(IMC,2)} -> esto nos permite definir solo 2 digitos adicionales en decimales - devuelve un número

print(
    f"IMC es: {IMC:.2f}"
)  # {IMC:.2f} -> esto nos permite definri solo 2 digitos decimales - devuelve una cadena de texto


#! ================================================================================================================

# * EJERCICIO 4: INFORMACIÓN PERSONAL:
# 1. Crea 5 variables con tu información:
# - nombre, edad, ciudad, profesion_deseada, lenguaje_favorito
# 2 Imprime un párrafo usando f-strings con toda la info ingresada.

#! Tu código aqui: aqui iniciamos a codear

nombre = "Edinson"
edad = 39
ciudad = "Lima"
profesion_deseada = "Programador"
lenguaj_favorito = "Python"

print(
    f"Mi nombres es {nombre}, tengo {edad}, soy de {ciudad}, mi profesión es {profesion_deseada} y mi lenguaje favorito es {lenguaj_favorito}"
)

#! ================================================================================================================

# * EJERCICIO 5: OPERACIONES MATEMÉTICAS:
# 1. Pide dos números al usuario
# 2. Muestra: suma, resta, multiplicación, división y potencia
# 3. Formato: "10 + 5 = 15"

#! Tu código aqui: aqui iniciamos a codear

numero_uno = int(input("Ingrese un número:\n"))
numero_dos = int(input("Ingrese otro número:\n"))

# suma = numero_uno + numero_dos
# resta = numero_uno - numero_dos
# multiplicacion = numero_uno * numero_dos
# division = numero_uno / numero_dos
# potencia = numero_uno ** numero_dos

# print(f'{numero_uno} + {numero_dos} = {suma}')
# print(f'{numero_uno} - {numero_dos} = {resta}')
# print(f'{numero_uno} * {numero_dos} = {multiplicacion}')
# print(f'{numero_uno} / {numero_dos} = {division}')
# print(f'{numero_uno} ** {numero_dos} = {potencia}')

print(f"{numero_uno} + {numero_dos} = {numero_uno + numero_dos}")
print(f"{numero_uno} - {numero_dos} = {numero_uno - numero_dos}")
print(f"{numero_uno} * {numero_dos} = {numero_uno * numero_dos}")
print(f"{numero_uno} / {numero_dos} = {numero_uno / numero_dos}")
print(f"{numero_uno} ** {numero_dos} = {numero_uno ** numero_dos}")

#! ================================================================================================================

# * EJERCICIO EXTRA:
# Crea un programa que:
# 1. Pida nombre, edad y ciudad.
# 2. Calcule en que año cumpliras 100 años
# 3. Muestre un mensaje: "Hola {nombre} de {ciudad}, cumpliras 100 años en el año {año}"

#! Tu código aqui: aqui iniciamos a codear

nombre_opcional = input("Ingrese su nombre\n")
edad_opcional = int(input("Ingrese su edad\n"))
ciudad_opcional = input("Ingrese su ciudad\n")

ACTUAL_OPCIONAL = 2026
calculo_ano = 100 - edad_opcional

ano = 2026 + calculo_ano

print(
    f"Hola {nombre_opcional} de {ciudad_opcional}, cumpliras 100 años en el año {ano}"
)
