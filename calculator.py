import math


def suma(x,y):
    print("El resultado de sumar " + str(x)+" y " + str(y)+" es: "+ str((x+y)))
    
def resta(x,y):
    print("El resultado de restar " + str(x)+" y " + str(y)+" es: "+ str((x-y)))
    
def multiplicacion(x,y):
    print("El resultado de multiplicar " + str(x)+" y " + str(y)+" es: "+ str((x*y)))
    
def division(x,y):
    print("El resultado de la division entre " + str(x)+" y " + str(y)+" es: "+ str((x/y)))
     
def exponencial(x):
    
    print("El exponencial de: "+ str(x) +" es: "+ str(math.exp(x)))

   

def menu():
    print(" ")
    print(" ")
    print(" ")
    print(" **** CALCULADORA PYTHON - BECAS DIGITALIZA - CISCO **** ")
    print(" ")
    print(" ")
    print(" Seleccione una opcion: ")
    
    operaciones = { '1': 'Sumar', '2': 'Restar', '3': 'Multiplicar', '4': 'Dividir','5': 'Exponencial','6':'Salir'}
    
    for key in operaciones:
        print(key, ' - ', operaciones[key])
    
    
   


def opciones():
    print(" Opciones de la calculadora: ")
    return int(input(" Introduce una opcion (1-6):  "))


    

while(True):
    menu()
    opcion=opciones()
    
    if (opcion==6):
        break
    else:
        numero1=int(input("Introduzca el primer numero: "))
        numero2=int(input("Introduzca el segundo numero: "))
        
        if(opcion==1):
            suma(numero1, numero2)
        elif(opcion==2):
            resta(numero1, numero2)
        elif(opcion==3):
            multiplicacion(numero1, numero2)
        elif(opcion==4):
            try:
                division(numero1, numero2)
            except ZeroDivisionError:
                print("No se puede dividir por 0 ")
            
        elif(opcion==5):
            exponencial(numero1)
        else:
            print("Opcion incorrecta, por favor seleccione una opcion valida ")


print("Gracias por usar nuestra aplicacion de calculadora")
    
    

