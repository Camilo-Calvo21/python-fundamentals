tasks = []

def add_task(tasks, title):
    title = title.strip()
    if title == "":
        print("Error: No se ingresó tarea")
        return
    new_task = {
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    print(f"La tarea '{title}' se agregó correctamente")

def list_tasks(tasks):
    if len(tasks) == 0:
        print("No hay tareas todavía.")
        return
    for current_task in tasks:
        if current_task["completed"]:
            status_text = "completado"
        else:
            status_text = "pendiente"

        print(f"{current_task['title']} - {status_text}")

def complete_task(tasks, task_number):
    try:
        num_index = int(task_number) - 1
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return
    if num_index < 0 or num_index >= len(tasks):
        print("Error: Esta tarea no existe.")
        return
    tasks[num_index]["completed"] = True
    print("Tarea completada con éxito!")

while True:
    print("=== Gestor de tareas ===")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Salir")
    task_option = input('Elige una opción: ')

    if task_option == "1":
        title_add = input("Nombre de la tarea: ")
        add_task(tasks, title_add)

    elif task_option == "2":
        list_tasks(tasks)

    elif task_option == "3":
        task_to_complete = input("Qué número quieres completar? ")
        complete_task(tasks, task_to_complete)

    elif task_option == "4":
        print("Hasta luego")
        break

    else:
        print("La opcion no fue seleccionada")
