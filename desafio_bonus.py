# ============================================================
# ? MINI DESAFÍO ANTES DE LA LECCIÓN 2
# ============================================================

# * EJERCICIO DESAFIO:
# Programa que calcule cuántos días has vivido aproximadamente
# Pide: año, mes y día de nacimiento
# Calcula: días totales vividos (aproximado)
# Tip: 1 año  = 365 días, 1 mes = 30 días

#! Aquí iniciamos a codear

dia_nacimiento = int(input('Ingrese el día de su nacimiento:\n'))
mes_nacimiento = int(input('Ingrese el mes de nacimiento:\n'))
ano_nacimiento = int(input('Ingrese el año de nacimiento:\n'))

ANO_ACTUAL = 2026

resta = ANO_ACTUAL - ano_nacimiento

total_ano = resta * 365

print(f'Días totales vividos son: {total_ano}')