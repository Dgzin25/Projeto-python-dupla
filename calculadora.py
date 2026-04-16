#estrutura da calculadora
import math
def calculadora():
    while True:
        print('''
===========MENU============
0 - para retornar ao menu       
1 - Soma
2 - subtrair
3 - Multiplicar
4 - Divisão
5 - Raiz quadrada
        ''')
        num = int(input("digite um numero da operção: "))
        if num == 0:
            return
        if num == 1:
            soma()
        elif num == 2:
            subtracao()
        elif num == 3:
            multiplicacao()
        elif num == 4:
            divisao()
        elif num == 5:
            raiz_quadrada()
        else:
            print("numero invalido")

#-------------Funções das operações--------------
def soma():
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 + num2
    print(f"o resultado da soma é {resultado}")
def subtracao():
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 - num2
    print(f"resultado da subtração é {resultado}")
def multiplicacao():
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 * num2
    print(f"resultado da multiplicação é {resultado}")
def divisao():
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 / num2
    print(f"resultado da divisão é {resultado}")
def raiz_quadrada():
    num1 = float(input("digite um numero: "))
    resultado = math.sqrt(num1)
    print(f"A raiz quadrada do numero {num1} é {resultado}")