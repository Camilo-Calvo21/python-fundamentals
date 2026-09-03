saludo = "Hola bienvenido a jugar"
numero1 = int(input("Escribe tu primer numero: "))
numero2 = int(input("Escribe tu segundo numero: "))
operacion = input("Elige una de las siguientes operaciones (+, -, *, /): ")
if operacion == "+":
    print(numero1 + numero2)
elif operacion == "-":
    print(numero1 - numero2)
elif operacion == "*":
    print(numero1 * numero2)
elif operacion == "/" and numero2 == 0:
    print("ZeroDivisionError: division by zero")
elif operacion == "/" :
    print(numero1 / numero2)    
else: 
    print("No selecionaste bien la operacion")    

