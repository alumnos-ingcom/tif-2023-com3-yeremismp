## g) Si el usuario selecciona la opción 3, le permitirá realizar conversiones de números enteros 
# positivos de a lo sumo 4 dígitos, teniendo tres opciones: “Binario”, “Hexadecimal” u “Octal” de un 
# número dado en el sistema de numérico decimal. Para evaluar y mostrar el resultado de la 
# conversión se debe presionar el botón “bin“, “hex” u “oct”. Luego de ello se finaliza la operación.
# En caso de que requiera realizar otra operación deberá regresar al paso c.

lista_RSL = []

def bin(a):
    if(a>1):
        while(a>1):    
            r = a % 2
            a = a // 2
            lista_RSL.append(r)
    
    lista_RSL.append(a)

def hex(a):
    if(a>15):
        while(a>15):    
            r = a % 16
            a = a // 16
            lista_RSL.append(r)
    
    lista_RSL.append(a)

def oct(a):
    if(a>7):
        while(a>7):    
            r = a % 8
            a = a // 8
            lista_RSL.append(r)  
    lista_RSL.append(a)

def solo_int(entrada):
    while (entrada):
        try:
            numero = int(entrada)
        except:
            entrada = input("ingrese un número\n")
        else:
            entrada = False 
    entrada = numero        
    return int(entrada)   
   
def Seleccionar(entrada):
    """esta funcion retorna un numero entero [1,3]"""
    while entrada:
        try:
            numero = int(entrada)
        except:
            entrada = input("ingrese una opcion correcta\n")
        else: 
            if numero >= 1 and numero <= 3:
                entrada = False
            else:
                entrada = input("ingrese una opcion correcta\n")
    return int(numero)

# Solicitar el numero que desea convertir al usuario
valor1 = input("Ingrese el numero que desea convertir:\n ")
resultado = solo_int(valor1)


operador = input("Ingrese a que desea convertir su numero (1) Bin (2) Hex (3) Oct \n")
operador = Seleccionar(operador)

if operador == 1:
    bin(resultado) 
elif operador == 2:
    hex(resultado)
elif operador == 3:
    oct(resultado)
else:
    print("Ingrese una opcion valida")

# Mostrar el resultado final
print(f"El resultado es:")
c = len(lista_RSL)
print(" [", end=" ")
while(c>0):
    if(lista_RSL[int(c-1)] > 9):
        if lista_RSL[int(c-1)] == 10:
            print("A", end=" ")
        elif lista_RSL[int(c-1)] == 11:
            print("B", end=" ")
        elif lista_RSL[int(c-1)] == 12:
            print("C", end=" ")
        elif lista_RSL[int(c-1)] == 13:
            print("D", end=" ")
        elif lista_RSL[int(c-1)] == 14:
            print("E", end=" ")
        else: 
            print("F", end=" ")
    else:
        print(lista_RSL[int(c-1)], end=" ")

    c = c - 1
print("]")