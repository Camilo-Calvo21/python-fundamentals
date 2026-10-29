import random
numero = random.randint(1, 100)
intentos = 1
print('Tienes que adivinar el numero que estoy pensado')
usuario = int(input("Escribe el numero: "))
while usuario != numero :
    if usuario < numero :
        print("mayor")
    elif usuario > numero :
        print("Menor")
    intentos += 1     
    usuario = int(input("Numero: "))
print("FELICITACIONES")    
print(f'Utilizaste {intentos} Intentos.') 