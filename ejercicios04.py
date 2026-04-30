# EJERCICIOS PRÁCTICOS

# ! Ejercicio 1: Gestor de tareas

# ? Crea un programa que:
# ? 1. Permita agregar tareas a una lista
# ? 2. Mostrar todas las tareas con números
# ? 3. Marcar tarea como completada (eliminarla)
# ? 4. Mostrar cuántas tareas quedan
# * Usa un menú con while

# todo Tú código aquí:

tareas = []

print('*'*50)
print('\n'+'📋 GESTOR DE TAREAS'.center(50))
print('*'*50)

while True:
    menu_accion = input(
        "\n1. Agregar Tarea\n2. Mostrar tarea\n3. Eliminar Tarea completada\n4. Tareas pendientes\n5. Salir\nIngresa una opción (1-2-3-4-5): ")
    print('-'*50)

    if menu_accion == "1":
        add_lista = input("¿Qué tarea desea ingresar: ")
        tareas.append(add_lista)
        print('-'*50)
        print('\n'+ f"✅ {add_lista} Agregado con exito".center(50))
        print('-'*50)

    elif menu_accion == "2":
        if not tareas:
            print('\n'+ f"⛔ Aun no hay datos.".center(50))
            print('-'*50)
        else:
            print('\n'+ f"📚🎧☕ Lista de Tareas".center(50))
            print('-'*50)
            for i, tarea in enumerate(tareas, start=1):
                print(f'{i}. {tarea}.')
            print('-'*50)

    elif menu_accion == '3':
        tarea_completa = input("¿Qué tarea esta completa?: ")
        indice = tareas.index(tarea_completa)
        tareas.pop(indice)
        print("-" * 50)
        print("\n" + f"❌ {tarea_completa} completado con exito.".center(50))
        print("-" * 50)

    elif menu_accion == '4':
        if not tareas:
            print("\n" + f"🔥 todas las tareas estan completas.".center(50))
            print("-" * 50)
        else:
            print("\n" + f"📌 Tareas pendientes: {len(tareas)}".center(50))
            print("-" * 50)
            for i, tarea in enumerate(tareas, start=1):
                print(f'{i}. {tarea}.')

    elif menu_accion == '5':
        print("🔥 Gracias por usar el gestor de tareas.🔥")
        break

    else:
        print('Opción invalida')
