def simplificar_fraccion(num, den):
    def calcular_mcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    mcd = calcular_mcd(num, den)
    numerador_simplificado = num // mcd
    denominador_simplificado = den // mcd

    return numerador_simplificado, denominador_simplificado

def sumar_fracciones(num1, den1, num2, den2):
    num = (num1 * den2) + (num2 * den1)
    den = den1 * den2
    return simplificar_fraccion(num, den)

def restar_fracciones(num1, den1, num2, den2):
    num = (num1 * den2) - (num2 * den1)
    den = den1 * den2
    return simplificar_fraccion(num, den)

def multiplicar_fracciones(num1, den1, num2, den2):
    num = num1 * num2
    den = den1 * den2
    return simplificar_fraccion(num, den)

def dividir_fracciones(num1, den1, num2, den2):
    num = num1 * den2
    den = den1 * num2
    return simplificar_fraccion(num, den)

def solo_float(entrada):
    while (entrada):
        try:
            numero = int(entrada)
        except:
            entrada = input("ingrese un número\n")
        else:
            entrada = False 
    entrada = numero        
    return int(entrada)

# Solicitamos los valores de la primer fraccion
num1 = input("Ingrese el numerador del primer valor: ")
den1 = input("Ingrese el denominador del primer valor: ")
num1 = solo_float(num1)
den1 = solo_float(den1)

salida = False
while salida is False:
    #Solicitamos operador
    operador = input("Ingrese el operador (+, -, *, /) o '=' para obtener el resultado: \n")
    
    
    if operador == "=":
        salida = True
    else:

        if operador == '+':
             #Solicitamos los valores de la segunda fraccion 
            num2 = input("Ingrese el numerador del segundo valor: ")
            den2 = input("Ingrese el denominador del segundo valor: ")
            num2 = solo_float(num2)
            den2 = solo_float(den2)
            resultado = sumar_fracciones(num1, den1, num2, den2)
        elif operador == '-':
            num2 = input("Ingrese el numerador del segundo valor: ")
            den2 = input("Ingrese el denominador del segundo valor: ")
            num2 = solo_float(num1)
            den2 = solo_float(den2)
            resultado = restar_fracciones(num1, den1, num2, den2)
        elif operador == '*':
            num2 = input("Ingrese el numerador del segundo valor: ")
            den2 = input("Ingrese el denominador del segundo valor: ")
            num2 = solo_float(num2)
            den2 = solo_float(den2)
            resultado = multiplicar_fracciones(num1, den1, num2, den2)
        elif operador == '/':
            num2 = input("Ingrese el numerador del segundo valor: ")
            den2 = input("Ingrese el denominador del segundo valor: ")
            num2 = solo_float(num2)
            den2 = solo_float(den2)
            resultado = dividir_fracciones(num1, den1, num2, den2)
        else:
            print("Operador inválido.")

num_resultado, den_resultado = resultado
numerador_simplificado, denominador_simplificado = simplificar_fraccion(num_resultado, den_resultado)

if denominador_simplificado == 1:
    resultado = numerador_simplificado
else:
    resultado = f"{numerador_simplificado}/{denominador_simplificado}"

print(resultado)
