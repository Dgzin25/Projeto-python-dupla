#estrutura da calculadora
import time
import math
import utilitarios
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
6 - historico de calculos
        ''')
        num = int(input("digite um numero da operção: "))
        if num == 0:
            arquivo = open("dados/log_calculadora.txt", "w") # formatando o historico da calculadora
            arquivo.close()
            return
        if num == 1:
            utilitarios.limpa_tela()
            soma()
        elif num == 2:
            utilitarios.limpa_tela()
            subtracao()
        elif num == 3:
            utilitarios.limpa_tela()
            multiplicacao()
        elif num == 4:
            utilitarios.limpa_tela()
            divisao()
        elif num == 5:
            utilitarios.limpa_tela()
            raiz_quadrada()
        elif num == 6:
            arquivo = open("dados/log_calculadora.txt", "r")
            utilitarios.limpa_tela()
            print(f"HISTORICO DE CALCULOS, \n{arquivo.read()}")
            arquivo.close
            time.sleep(5)
        else:
            utilitarios.limpa_tela()
            print("numero invalido")

#-------------Funções das operações--------------
def soma():
    arquivo = open("dados/log_calculadora.txt", "a") # abrindo arquivo de log 
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 + num2
    arquivo.write(f"{num1} + {num2} = {resultado}\n") #adicionando as log 
    arquivo.close() # fechando arquivo de log
    print(f"o resultado da soma é {resultado}")
def subtracao():
    arquivo = open("dados/log_calculadora.txt", "a") # abrindo arquivo de log 
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 - num2
    arquivo.write(f"{num1} - {num2} = {resultado}\n") #adicionando as log 
    arquivo.close() # fechando arquivo de log
    print(f"resultado da subtração é {resultado}")
def multiplicacao():
    arquivo = open("dados/log_calculadora.txt", "a") # abrindo arquivo de log 
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 * num2
    arquivo.write(f"{num1} x {num2} = {resultado}\n") #adicionando as log 
    arquivo.close() # fechando arquivo de log
    print(f"resultado da multiplicação é {resultado}")
def divisao():
    arquivo = open("dados/log_calculadora.txt", "a") # abrindo arquivo de log 
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    resultado = num1 / num2
    arquivo.write(f"{num1} / {num2} = {resultado}\n") #adicionando as log 
    arquivo.close() # fechando arquivo de log
    print(f"resultado da divisão é {resultado}")
def raiz_quadrada():
    arquivo = open("dados/log_calculadora.txt", "a") # abrindo arquivo de log 
    num1 = float(input("digite um numero: "))
    resultado = math.sqrt(num1)
    arquivo.write(f"√{num1} = {resultado}\n") #adicionando as log 
    arquivo.close() # fechando arquivo de log
    print(f"A raiz quadrada do numero {num1} é {resultado}")