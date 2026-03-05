# ===============================================
# ! EJERCICIOS PRÁCTICOS:
# ===============================================

# ***********************************************
# * Ejercicio 1: Verificador de Edad
# ***********************************************

# Pide la edad al usuario
# Si es menor de 13: "Eres un niño"
# Si tiene entre 13 y 17: "Eres adolecente"
# Si tiene entre 18 y 59: "Eres un adulto"
# Si tiene 60 o más: "Eres un adulto mayor"

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------

# print('*' * 50)
# print('EJERCICIOS PRÁCTICOS'.center(50))
# print('*' * 50)

# edad = int(input('Ingrese su edad:\n'))

# if edad >= 0 and edad < 13:
#     print(f'Eres un niño con {edad} años')
# elif edad >= 13 and edad <= 17:
#     print(f'Eres un adolecente con {edad} años')
# elif edad >= 18 and edad <= 59:
#     print(f'Eres un adulto con {edad} años')
# elif edad >= 60:
#     print(f'Eres un adulto mayor con {edad} años')
# else:
#     print('Edad invalida')

# ***********************************************
# * Ejercicio 2: Calculadora Simple con Operador
# ***********************************************

# Pide dos números al usuario
# Pide una operación: +, -, *, /
# Según la operación, realiza el cálculo correspondiente
# Muestra el resultado
# Si la operción no es válida, muestra un mensaje de error

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------

# print('=' * 50)
# print('CALCULADORA SIMPLE'.center(50))
# print('=' * 50)
# numero_uno = int(input('Ingrese un número: '))
# numero_dos = int(input('Ingrese otro número: '))

# operacion = input('¿Qué operación deseas hacer?\nA. Suma\nB. Resta\nC. Multiplicación\nD. División\nSolo elige una opción: ')

# if operacion.upper() == 'A':
#     suma = numero_uno + numero_dos
#     print(f'El resultado de la suma de {numero_uno} + {numero_dos} es: {suma}')
# elif operacion.upper() == 'B':
#     resta = numero_uno - numero_dos
#     print(f"El resultado de la resta de {numero_uno} - {numero_dos} es: {resta}")
# elif operacion.upper() == 'C':
#     multiplicacion = numero_uno * numero_dos
#     print(f"El resultado de la multiplicación de {numero_uno} * {numero_dos} es: {multiplicacion}")
# elif operacion.upper() == 'D':
#     division = numero_uno / numero_dos
#     print(
#         f"El resultado de la division de {numero_uno} / {numero_dos} es: {division}"
#     )
# else:
#     print('Operación invalida')

# ***********************************************
# * Ejercicio 3: Verifcador de contraseña
# ***********************************************

# Define una contraseña correcta (por ejemplo: "Python123")
# Pide al usuario que ingrese la contraseña
# Si es correcta: "Acceso permitido"
# Si es incorrecta: "Acceso denegado"
# Bonus: Ignora mayúsculas / minúsculas

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------

print('*' *50)
print('VERIFICADOR DE CONTRASEÑA'.center(50))
print('*' * 50)

contrasena_correcta = 'Python2026'

password= input('Ingrese su contraseña: ').upper()

if password == contrasena_correcta.upper():
    print('Bienvenido acceso permitido')
else:
    print('Acceso denegado password incorrecto')

# ***********************************************
# * Ejercicio 4: Descuento en Tienda
# ***********************************************

# Pide el monto de compra al usuario
# Pide si es estudiante (si/no)
# Si la compra es mayor a 100 y es estudiante: 20% descuento
# Si la compra es mayor a 100 y NO es estudiante: 10% descuento
# Si la compra es menor a 100  y es estudiante: 5% descuento
# Si la compra es menor a 100 y NO es estudiante: sin descuento
# Muestra el total a pagar después del desuento

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------

print('=' * 25)
print('TIENDA'.center(25))
print('=' * 25)

monto = int(input('Ingrese el monto de compra: '))
es_estudiante = input('¿Es estudiante?\nIngrese: S = si | N =no: ').upper()

if monto >= 100 and es_estudiante == 'S':
    descuento = monto * 0.2
    total_pagar = monto - descuento
    print(f'Por tu compra tienes un descuento de {descuento} y tu total a pagar es de {total_pagar}')
elif monto >= 100 and es_estudiante == 'N':
    descuento = monto * 0.1
    total_pagar = monto - descuento
    print(f'Por tu compra tienes un descuento de {descuento} y tu total a pagar es de {total_pagar}')
elif monto < 100 and es_estudiante == 'S':
    descuento = monto * 0.05
    total_pagar = monto - descuento
    print(f'Por tu compra tienes un descuento de {descuento} y tu total a pagar es de {total_pagar}')
elif monto < 100 and es_estudiante == 'N':
    print(f'Tu total a pagar es de {monto}')

# ***********************************************
# * Ejercicio 5: Año Bisiesto
# ***********************************************

# Pide un año al usuario
# Un año es bisiesto si:
#   - Es divisible por 4 y
#   -(NO es divisible por 100 o es divisible por 400)
# Ejemplos: 2024 es bisiesto, 2023 no, 2000 si, 1900 no
# Muestra si el año es bisiesto o no

# ! Pista: usa el operador % (módulo) para verificar divisibilidad
# ! Si año % 4 == 0, entonces es divisible por 4

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------

print('+' * 50)
print('AÑO BISIESTO'.center(50))
print("+" * 50)

dato = int(input('Ingrese un año: '))

if dato % 4 == 0 and (dato % 100 != 0 or dato % 400 ==0):
    print(f'El año ingresado {dato} es bisiesto')
else:
    print(f'El año ingresado {dato} no es biciesto')

# ***********************************************
# * Ejercicio 6: Clasificador de Números
# ***********************************************

# Pide un número al usuario
# Indica si es:
#   - Positivo, negativo o cero
#   - Par o impar (solo si no es cero)
# Ejemplo de salida: "El número 7 es positivo e impar"

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------
print('=' * 50)
print('Clasificador de números'.center(50))
print("=" * 50)

user_numero = int(input('Ingrese un número: '))

if user_numero > 0:
    if user_numero % 2 == 0:
        print(f'El número {user_numero} es positivo y par')
    else:
        print(f'El número {user_numero} es positivo e impar')
elif user_numero < 0:
    if user_numero % 2 == 0:
        print(f'El número {user_numero} es negativo y par')
    else:
        print(f'El número {user_numero} es negativo e impar')
else:
    print(f'El número es cero')

# ***********************************************
# * Ejercicio 7: Sistema de Calificaciones Mejorado
# ***********************************************

# Pide una calificación (0-100)
# Muestra la letra correspondiente:
#   90 - 100: A
#   80 - 89: B
#   70 - 79: C
#   60 - 69: D
#   0 - 59: F
# Además, si la calificación no está en el rango 0 - 100,
# muestra "Calificación inválida"

# ? ----------------------------------------------
# todo tu código aquí:
# ? ----------------------------------------------
print('=' * 50)
print('SISTEMA DE CALIFICACIÓN'.center(50))
print("=" * 50)

calificacion = int(input('Ingrese su calificación: '))

if calificacion >= 90 and calificacion <= 100:
  print('Calificación es: A')
elif calificacion >= 80 and calificacion <= 89:
  print('Calificción es: B')
elif calificacion >= 70 and calificacion <= 79:
  print('Calificación es: C')
elif calificacion >= 60 and calificacion <= 69:
  print('Calificación es: D')
elif calificacion >= 0 and calificacion <= 59:
  print('Calificación es: F')
else:
  print(f'Calificación {calificacion}, es invalida')