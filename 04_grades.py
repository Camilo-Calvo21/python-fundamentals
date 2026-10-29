print("Calcula tu promedio de notas. ")
total_notas = int(input("Ingresa el numero de notas totales: "))

if total_notas <= 0:
    print("El número de notas debe ser mayor a 0. Saliendo del programa.")
else:
    notas = []
    for recorrido in range(1, total_notas + 1):
        nota = float(input("Escribe la nota: "))
        notas.append(nota)

    promedio = sum(notas) / total_notas
    
    if promedio >= 3.0:
        print("Aprueba") 
    else:
        print("Reprueba")    
    
    alta = max(notas)
    baja = min(notas)
    
    print(f'Tu promedio de notas es: {promedio}')
    print(f'Tu nota mas alta fue: {alta}')
    print(f'Tu nota mas baja fue: {baja}')