print("Calcula tu prodemio de notas. ")
total_notas = int(input("Ingresa el numero de notas totales: "))
notas = []
for recorrido in range(1, total_notas + 1):
    nota = float(input("Escribe la nota: "))
    notas.append(nota)
    promedio = sum(notas)/ total_notas
if promedio >= 3.0 :
    print("Aprueba") 
elif promedio < 3.0 :
    print("Reprueba")    
alta = max(notas)
baja = min(notas)
print(f'Tu promedio de notas es: {promedio}')
print(f'Tu nota mas alta fue: {alta}')
print(f'Tu nota mas baja fue: {baja}')