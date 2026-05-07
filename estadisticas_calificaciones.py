import os
os.system("cls" if os.name == 'nt' else 'clear')

# Ejercicio 04
# ! Estadisticas de Calificaciones
# ? Pide al usuario 5 calificaciones (0 - 100)
# ? Guardalas en una lista
# ? Muestra:
#   - Todas las calificaciones
#   - Promedio
#   - Calificación más alta
#   - Calificación más baja
#   - Cuantas estan por encima del promedio

# todo Tú código aquí:

calificaciones = []
print('-'*50)
print("💯 CALIFICACIONES".center(50))
print('-'*50)

# Solicita 5 calificaciones con validación
while len(calificaciones) < 5:
    try:
        nota = int(input("Ingrese una calificación: "))
        if nota >= 0 and nota <= 100:
            calificaciones.append(nota)
            print(f"✅ La nota {nota}, fue ingresada con éxito.\n")
        else:
            print(f"⛔ {nota} no es valida debe estar entre 0 y 100\n")
    except ValueError:     # Al ingresar letras u otro carcater arrojara el error
        print(f"❌ Error debes ingresar un número valido\n")
print('-'*50)

# Muestra las calificaciones
print("📝 LISTA DE CALIFICACIONES".center(50))
print("-" * 50)
for i, nota in enumerate(calificaciones, start=1):    # Enumera las calificaciones del 1 al 5
  print(f'{i}. {nota}')
print('-'*50)

# Calcular estadisticas
promedio = sum(calificaciones) / len(calificaciones)
print(f"📊 Promedio: {promedio:.2f}".center(50))
print("-" * 50)
print(f"⬆️  Calificación más alta: {max(calificaciones)}")
print(f"⬇️  Calificación más baja: {min(calificaciones)}")
print("-" * 50)

# Notas por encima del promedio
maspromedio = []
for nota in calificaciones:
    if nota > promedio:
        maspromedio.append(nota)
        print(f"🔢 {nota} esta por encima del promedio")
print("-" * 50)

mensaje = 'nota' if len(maspromedio) == 1 else 'notas'     # Mensaje ternario para uso de singular y plural
print(f"🏅 {len(maspromedio)} {mensaje} están por encima del promedio".center(50))
print("-" * 50)
