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

print('*' * 50)
print('EJERCICIOS PRÁCTICOS'.center(50))
print('*' * 50)

edad = int(input('Ingrese su edad:\n'))

if edad >= 0 and edad < 13:
  print(f'Eres un niño con {edad} años')
elif edad >= 13 and edad <= 17:
  print(f'Eres un adolecente con {edad} años')
elif edad >= 18 and edad <= 59:
  print(f'Eres un adulto con {edad} años')
elif edad >= 60:
  print(f'Eres un adulto mayor con {edad} años')
else:
  print('Edad invalida')