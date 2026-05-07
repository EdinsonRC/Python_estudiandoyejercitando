import os
os.system('cls')
# EJERCICIOS PRÁCTICOS

# ! Ejercicio 1: Gestor de tareas

# ? Crea un programa que:
# ? 1. Permita agregar tareas a una lista
# ? 2. Mostrar todas las tareas con números
# ? 3. Marcar tarea como completada (eliminarla)
# ? 4. Mostrar cuántas tareas quedan
# * Usa un menú con while

# todo Tú código aquí:

tareas = []    # Se crea la lista

print('*'*50)
print('\n'+'📋 GESTOR DE TAREAS'.center(50))
print('*'*50)

# Menú de acciones
while True:
    menu_accion = input(
        "\n1. Agregar Tarea\n2. Mostrar tarea\n3. Eliminar Tarea completada\n4. Tareas pendientes\n5. Salir\nIngresa una opción (1-2-3-4-5): ")
    print('-'*50)    # Realiza la pregunta al usuario

    if menu_accion == "1":     # Si usuario elige la opción 1
        add_lista = input("¿Qué tarea desea ingresar: ")     # La variable lista solicita al usuario que tarea desea ingresar para almacenar en la lista
        tareas.append(add_lista)    # .append para agregar a la lista la tarea ingresada por el usuario en la variable add_lista
        print('-'*50)
        print('\n'+ f"✅ {add_lista} Agregado con exito".center(50))     # Mensaje agregado con exito
        print('-'*50)

    elif menu_accion == "2":    # Si usuario elige la opción 2
        if not tareas:     # Si "No" hay tareas
            print('\n'+ f"⛔ Aun no hay datos.".center(50))
            print('-'*50)
        else:
            print('\n'+ f"📚🎧☕ Lista de Tareas".center(50))
            print('-'*50)
            for i, tarea in enumerate(tareas, start=1):     # "Para i, variable in enumerate(lista, start=1)"  las tareas agregadas a la lista inician(start) desde 1 
                print(f'{i}. {tarea}.')     # "1. tarea"
            print('-'*50)

    elif menu_accion == '3':    # Si usuario elige la opción 3
        tarea_completa = input("¿Qué tarea esta completa?: ")    # Ingresa el nombre de la tarea terminada y lo almacena en la variable tarea_completa
        indice = tareas.index(tarea_completa)     # La variable indice almacena el indice donde se encuentra la tarea, tareas.index(tarea_completa) donde tareas es la lista y index es la posición de la tarea que se ingreso en la variable de tarea_completa.
        tareas.pop(indice)     # Esta linea elimina el indice "tareas.pop(indice)" donde tareas es la 
        print("-" * 50)
        print("\n" + f"❌ {tarea_completa} completado con exito.".center(50))
        print("-" * 50)
        
    elif menu_accion == '4':    # Si usuario elige la opción 4
        if not tareas:     # Si "NO" hay tareas
            print("\n" + f"🔥 todas las tareas estan completas.".center(50))
            print("-" * 50)
        else:
            print("\n" + f"📌 Tareas pendientes: {len(tareas)}".center(50))    # Con "len" puedes mostrar las cantidad de tareas en la lista
            print("-" * 50)
            for i, tarea in enumerate(tareas, start=1):     # "Para i, variable in enumerate(lista, start=1)"  las tareas agregadas a la lista inician(start) desde 1
                print(f'{i}. {tarea}.')

    elif menu_accion == '5':     # Si usuario elige la opción 5
        print("🔥 Gracias por usar el gestor de tareas.🔥")
        break     # termina el bucle

    else:
        print('Opción invalida')
