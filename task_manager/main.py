tasks = []

def add_task(tasks, title):
    new_task = {
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    print(f"La tarea '{title}' se agregó correctamente")

while True:
    print("=== Gestor de tareas ===")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Salir")
    task_option = input('Elige una opcion: ')

    if task_option == "1":
        title_add = input("Nombre de la tarea: ")
        add_task(tasks, title_add)
    elif task_option == "2":
        print("Lista de tareas: ")
    elif task_option == "3":
        print("Hasta luego")
        break
    else:
        print("La opcion no fue seleccionada")