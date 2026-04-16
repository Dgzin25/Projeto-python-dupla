#estrutura da calculadora
import math
def calculadora():
    while True:
        print('''
      ===========MENU============
         0 - Retornar ao menu
_______________________________________
|1 - Adição        |5 - Raiz Quadrada |
|2 - Subtração     |6 - Porcentagem   |
|3 - Multiplicação |7 - Fatorial      |
|4 - Divisão       |8 -               |
''')
        #* Evita erro caso o input seja uma valor não inteiro *
        try:
            num = int(input("digite um numero da operção: "))
            if num == 0:
                return
            elif num == 1:
                soma()
            elif num == 2:
                subtracao()
            elif num == 3:
                multiplicacao()
            elif num == 4:
                divisao()
            elif num == 5:
                raiz_quadrada()
            elif num == 6:
                porcentagem()
            elif num == 7:
                fatorial()
            else:
                print("Número Inválido")
        except ValueError:
            print("Entrada Inválida - *APENAS NÚMEROS INTEIROS*")

#-------------Funções das operações--------------
def soma():
    print("\n[+]Soma")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = num1 + num2
    if resultado.is_integer():
        print(f"O resultado da soma é: {int(resultado)}")    
    else:
        print(f"O resultado da soma é: {resultado}")

def subtracao():
    print("\n[+]Subtração")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = num1 - num2
    if resultado.is_integer():
        print(f"resultado da subtração é: {int(resultado)}")
    else:
        print(f"resultado da subtração é: {resultado}")

def multiplicacao():
    print("\n[+]Multiplicação")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = num1 * num2
    if resultado.is_integer():
        print(f"resultado da multiplicação é: {int(resultado)}")
    else:
        print(f"resultado da multiplicação é: {resultado}")

def divisao():
    print("\n[+]Divisão")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    #! condição para evitar divisão por 0, sem ela quebraria o código !
    if num2 == 0:
        print("Não existe divisão por 0\nTente Novamente...")
        return divisao()
    resultado = num1 / num2
    if resultado.is_integer():
        print(f"O resultado da divisão é: {int(resultado)}")
    else:
        print(f"O resultado da divisão é: {resultado}")

def raiz_quadrada():
    print("\n[+]Raiz Quadrada")
    num1 = float(input("Digite um número: "))
    #! condição para proibir numeros inteiros negativos !
    if num1 < 0:
        print("Não existe raiz quadrada negativa\nTente Novamente...")
    resultado = math.sqrt(num1)
    if resultado.is_integer():
        print(f"A raiz quadrada de {int(num1)} é: {int(resultado)}")
    else:
        print(f"A raiz quadrada de {num1} é: {resultado:.2f}")

def porcentagem():
    print("\n[+]Porcentagem")
    num1 = float(input("Digite um número: "))
    resultado = num1/100
    if resultado.is_integer():
        print(f"O resultado da porcentagem é: {int(resultado)}%")
    else:
        print(f"O resultado da porcentagem é: {resultado:.2f}%")

def fatorial():
    print("\n[+]Fatorial")
    num1 = int(input("Digite um número: "))
    if num1 < 0:
        print("Entrada Inválida - Apenas números inteiros positivos")
        return fatorial()
    else:
        resultado = math.factorial(num1)
        print(f"A fatorial de {num1} é: {resultado}")
calculadora()
#* A função "is_intenger()" é pra caso o número seja inteiro não ficar como float e sim inteiro (pra não confundir) *