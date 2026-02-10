# ==============================================================
# ? LECCIÓN 2: CONDICIONALES
# ==============================================================

# Las condicionales permiten que el programa tome DECISIONES
# Ejecutan diferetes bloques de código según una condición

# * ============================================================
# ? 1. ESTRUCTURA BÁSICA: if(SI)
# * ============================================================

# Sintaxis:
# if condición:
#     código que se ejecuta SI la condición es True

edad = 18  # Variable que usaremos para comparar

# Compraramos si la edad es mayor o igual a 18
if edad >= 18:  # Si edad es mayor o igual a 18
  print('Eres mayor de edad')  # Este código solo se ejecuta si la condición es True
  print('Puedes votar')  # La identación (4 espacios) indica que pertenece al if

# IMPORTANTE: La indentación en Python No es opcional
# todo el código que pertenece al if debe estar identado (4 espacios o 1 tab)

print('Este mensaje se imprime siempre')  # Sin indentación = fuera del if

# * ============================================================
# ? 2. OPERADORES DE COMPARACIÓN
# * ============================================================

# Estos operadores devuelven True o False (booleanos)

numero = 10

# == (igual a) - Compara si dos valores son iguales
print(numero == 10)  # True - número es igual a 10
print(numero == 5)   # False - número NO es igual a 5

# != (diferente de) - Compara si dos valores son diferentes
print(numero != 5)  # True - número es diferente de 5
print(numero != 10) # False - numero NO es diferente de 10

# > (mayor que)
print(numero > 5)   # True - 10 es mayor que 5
print(numero > 15)  # False - 10 NO es mayor que 15

# < (menor que)
print(numero < 15)   # True - 10 es menor que 15
print(numero < 5)    # False - 10 NO es menor que 5

# >= (mayor o igual que)
print(numero >= 10)   # True - 10 es igual a 10
print(numero >= 5)    # True - 10 es mayor que 5

# <= (menor o igual que)
print(numero <= 10)   # True - 10 es igual a 10
print(numero <= 15)   # True - 10 es menor que 15

# * ============================================================
# ? 3. ESTRUCTURA if - else (SI - SINO)
# # * ==========================================================

# Else ejecuta código cuando la condición del if es False
# Sintaxis:
# if condición:
#     código si True
# else:
#     código si False

edad = 15

if edad >= 18:   # Si edad es mayor o igual a 18
    print('Eres mayor de edad')   # Se ejecuta si es True
else:   # De lo contrario (si la condición es False)
    print('Eres menor de edad')   # Se ejecuta si es False

# Solo UNO de los dos bloques se ejecutará, nunca ambos

# * ============================================================
# ? 4. ESTRUCTURA if-elif-else (SI - SINO SI - SINO)
# # * ==========================================================

# elif permite verificar múltiples condiciones
# Se lee como: "si no se cumplió lo anterior, verifica esta otra condición"

nota = 85   # Calificación del estudiante

if nota >= 90:   # Primera condición
    print('Calificación: A - Excelente')
elif nota >= 80:   # Se verifica solo si la anterior fue False
    print('Calificación: B - Muy bueno')   # Esta se ejecutará
elif nota >= 70:   # Se verifica solo si las anteriores fueron False
    print('Calificación: C - Bueno')
elif nota >= 60:   # Se verifica solo si las anteriores fueron False
    print('Calificación: D - Suficiente')
else:   # Si ninguna condición anterior fue True
    print('Calificación: F - Reprobado')

# ! Python evalúa de arriba hacia abajo
# ! Cuando encuentra una condición True, ejecuta ese bloque y SALE
# ! No verifica las condiciones siguientes

# * ============================================================
# ? 5. OPERADORES LÓGICOS
# # * ==========================================================

# Permite combinar múliples condiciones

# * --- AND (y) - Ambas condiciones deben ser True ---
edad = 20
tiene_licencia = True

# Ambas condiciones deben cumplirse
if edad >= 18 and tiene_licencia == True :   # Mejor: tiene_licencia (sin == True)
  print('Puede conducir')
else:
  print('No puedes conducir')

# ? TABLA DE VERDAD AND (y):
# True and True = True
# True and False = False
# False and True = False
# True and False = False

# * --- OR (o) - Al menos UNA condición debe ser True ---
es_fin_de_semana = True
es_feriado = False

# Al menos una debe cumplirse
if es_fin_de_semana or es_feriado:
  print('¡Puedes descansar!')
else:
  print('Es día laboral')

# ? TABLA DE VERDAD OR(o):
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# * --- NOT (no) - Invierte el valor booleano ---
esta_lloviendo = False

# not invierte: False se convierte en True
if not esta_lloviendo:   # Si NO está lloviendo
    print('Puedes salir sin paraguas')
else:
    print('Lleva paraguas')

# not True = False
# not False = True

# * ============================================================
# ? 6. COMBINANDO OPERADORES LÓGICOS
# # * ==========================================================

edad = 25
tiene_dinero = True
tiene_tiempo = True

# Combinamos múltiples condiciones con and y or
if edad >= 18 and (tiene_dinero or tiene_tiempo):
  # Paréntesis () definen el orden de evaluación
  # Primero se evalúa (tiene_dinero or tiene_tiempo)
  # Luego se combina con la edad
  print('Puedes ir al cine')
else:
  print('No puedes ir al cine')

#! EJEMPLO COMPLEJO

temperatura = 32
es_verano = True
tiene_protector = False

if temperatura > 30 and es_verano and not tiene_protector:
    print("🚨 Hace mucho calor y no tienes protector solar")
elif temperatura > 30 and tiene_protector:
    print("✅ Hace calor pero estás protegido")
elif temperatura <= 30:
    print("🌥️ Temperatura agradable")

# * ============================================================
# ? 7. CONDICIONALES ANIDADAS
# # * ==========================================================

# Puedes poner un if dentro de otro if
# Útil para verificaciones más especificas

edad = 20
es_estudiante = True

if edad >= 18:   # Primera verificación
    print('Eres mayor de edad')

    if es_estudiante:   # Segunda verificación (dentro de la primera)
        print('Tienes descuento estudiantil')   # 2 niveles de indentación
    else:
        print('Pagas precio completo')
else:
    print('Eres menor de edad')
    print('No puedes acceder')

# ! IMPORTANTE: Cada nivel de anidación requiere 4 espacios adcionales

# * ============================================================
# ? 8. COMPARANDO STRINGS (TEXTOS)
# # * ==========================================================

nombre = 'Juan'

# Comparación exacta ( case-sensitive: distingue mayúsculas / minúsculas)
if nombre == 'Juan':   #True
  print('El nombre es Juan')

if nombre == 'juan':   #False - las mayúsculas importan
  print('Este mensaje NO se imprime')

# Todo Para ignorar mayúsculas / minúsculas, usa .lower() o .upper()
if nombre.lower() == 'juan':   # Convierte a minusculas antes de comparar (.lower() convierte en minuscula todo / .upper() convierte en MAYUSULA todo)
    print('El nombre es Juan (sin importar mayúsculas)')

"""
# .lower()	Todo en minúsculas
# .upper()	Todo en mayúsculas
# .capitalize()	Primera letra mayúscula
# .strip()	Quita espacios de los bordes
"""

# Verificar si un string está vacio
mensaje = ""

if mensaje == "":   # String vacio
  print('El mensaje esta vacio')

# Forma más "pythónica" (recomendada):
if not mensaje:   # Si mensaje es vacio, es False
    print('El mensaje está vacio (forma pythónica)')

# * ============================================================
# ? 9. OPERADOR IN - verificar pertenencia
# # * ==========================================================

# Verifica si un valor está dentro de una secuencia

vocales = 'aeiou'
letra = 'a'

if letra in vocales:   # Verifica si 'a' esta en 'aeiou'
  print(f'{letra} es una vocal')

# También funciona con números en rangos
edad = 25

if edad in range(18,65):   # range(18,65) genera números del 18 al 64
  print('Estas en edad laboral')

# Verificar si NO está (not in)
letra = 'z'

if letra not in vocales:
    print(f'{letra} no es una vocal')

# * ============================================================
# ? 10. EXPRESIONES CONDICIONALES (Ternario)
# # * ==========================================================

# Forma compacta de escribir if-else en una sola linea
# Sintaxis: valor_si_true if condicion else valor_si_false

edad = 20
# Forma tradicional:
if edad >= 18:
  estado = 'Mayor de edad'
else:
  estado = 'Menor de edad'

# Forma compacta (Ternaria)
estado = 'Mayor de edad' if edad >= 18 else 'Menor de edad'
print(estado)

# Otro ejemplo:
numero = 7
tipo = 'Par' if numero % 2 == 0 else 'Impar'
print(f'{numero} es {tipo}')

# * ============================================================
# ? 11. EJEMPLO PRÁCTICO: CALCULADORA IMC CON INTERPRETACIÓN
# # * ==========================================================

print('\n'+'='*50)
print('CLACULADORA DE IMC CON INTERPRETACIÓN'.center(50))
print('='*50)

peso = float(input('Ingresa tu peso en Kg: '))
altura = float(input('Ingresa tu altura en metros: '))

# Calcular IMC
imc = peso / (altura ** 2)

print(f'\n Tu IMC es: {imc:.2f}')

# Interpretar el resultado según rangos de la OMS
if imc < 18.5:
    print('Categoría: Bajo peso')
    print('Recomendación: Consulta con un nutricionista')
elif imc >= 18.5 and imc < 25:
    print('Categoria: Peso normal')
    print('Recomendación: ¡Sigue asi!')
elif imc >=25 and imc <30:
    print('Categoría: Sobrepeso')
    print('Recomendación: Considera hacer más ejercicio')
elif imc >= 30 and imc <35:
    print('Categoria: Obesidad Grado I')
    print('Recomendación: Consulta con un médico')
elif imc >= 35 and imc < 40:
    print('Categoría: Obesidad Grado II')
    print('Recomendación: Es imprtante consultar con un médico')
else:   # imc >= 40
    print('Categoría: Obesidad Grado III')
    print('Recomendacion: Consulta medica urgente recomendada')

# * ============================================================
# ? 12. VALORES TRUTHY Y FALSY
# # * ==========================================================
#! En Python, algunos valores se consideran False automáticamente:
# - None
# - False
# - 0 (cero)
# - 0.0 (Cero decimal)
# - "" (String vacio)
# - [] (Lista vacia)
# - {} (Diccionario vacio)
# - () (Tupla vacia)

# Todos los demás valores se consideran True

nombre = ""
if nombre:   # String vacio es False
  print("Hay un nombre")
else:
  print("No hay nombre")   # Esto se ejecuta

numero = 0
if numero: # 0 es False
  print("Número es diferente de cero")
else:
  print("Número es cero")   # Esto se ejecuta

# =====================================================
# ! RESUMEN DE ESTA LECCIÓN
# =====================================================

print('\n' + '=' * 50)
print('RESUMEN - LECCIÓN 2')
print('=' * 50)
print('1. if: ejecuta código si la condición es True')
print('2. else: ejecuta código si la condición es False')
print('3. elif: verifica otra condición si la anterior fue False')
print('4. Comparadores: ==, !=, >, <, >=, <=')
print('5. Lógicos: and(y), or(o), not (no)')
print('6. in/not in: verifica pertenecia')
print('7. Indentación: 4 espacios por cada nivel')
print('8. Valores falsy: None, False, 0, "", [], {},()')
print('=' * 50)