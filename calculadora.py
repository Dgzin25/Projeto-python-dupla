#estrutura da calculadora
import time
import math
import utilitarios
def salva_log(resultado, operacao, num1, num2):
    if resultado.is_integer():
        resultado = int(resultado)
    if num1.is_integer():
        num1 = int(num1)
    if num2.is_integer():
        num2 = int(num2)
    arquivo = open("dados/log_calculadora.txt", "a", encoding="utf-8")# utt-8 é modo mais atualizado
    #para nao da erro na raiz quadrada no simbolo
    if operacao == 1:
        arquivo.write(f"{num1} + {num2} = {resultado}\n") #adicionando as log
    elif operacao == 2:
        arquivo.write(f"{num1} - {num2} = {resultado}\n") #adicionando as log 
    elif operacao == 3:
        arquivo.write(f"{num1} x {num2} = {resultado}\n") #adicionando as log 
    elif operacao == 4: 
        arquivo.write(f"{num1} / {num2} = {resultado}\n") #adicionando as log
    elif operacao == 5:
        arquivo.write(f"√{num1} = {resultado}\n") #adicionando as log 
    arquivo.close() 
    return(resultado)

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
        try:
            num = float(input("digite um numero da operção: "))
        except ValueError:
            print("Entrada invalida, somente numeros!!")
            continue
#-------------------------------------------------------------
        if num == 6:
            arquivo = open("dados/log_calculadora.txt", "r", encoding="utf-8") #lendo o historico no modo utf-8 para ler os caracteres como da raiz quadrada
            utilitarios.limpa_tela()
            print(f"HISTORICO DE CALCULOS, \n{arquivo.read()}")
            arquivo.close()
            time.sleep(5)
            continue
#-------------------------------------------------------------------
        if num == 5:
            num1 = float(input("Digite o numero: "))
        else:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("digite o segundo numero: "))
        if num == 0:
            arquivo = open("dados/log_calculadora.txt", "w") # formatando o historico da calculadora
            arquivo.close()
            return
        if num == 1:
            utilitarios.limpa_tela()
            soma(num1, num2)
        elif num == 2:
            utilitarios.limpa_tela()
            subtracao(num1, num2)
        elif num == 3:
            utilitarios.limpa_tela()
            multiplicacao(num1, num2)
        elif num == 4:
            utilitarios.limpa_tela()
            divisao(num1, num2)
        elif num == 5:
            utilitarios.limpa_tela()
            raiz_quadrada(num1)
        else:
            utilitarios.limpa_tela()
            print("numero invalido")

#-------------Funções das operações--------------
def soma(num1, num2):
    resultado = num1 + num2
    operacao = 1
    resultado = salva_log(resultado, operacao, num1, num2)
    print(f"o resultado da soma é {resultado}")
def subtracao(num1, num2):
    resultado = num1 - num2
    operacao = 2
    resultado = salva_log(resultado, operacao, num1, num2)
    print(f"resultado da subtração é {resultado}")
def multiplicacao(num1, num2):
    resultado = num1 * num2
    operacao = 3
    resultado = salva_log(resultado, operacao, num1, num2)
    print(f"resultado da multiplicação é {resultado}")
def divisao(num1, num2):
    resultado = num1 / num2
    operacao = 4
    resultado = salva_log(resultado, operacao, num1, num2)
    print(f"resultado da divisão é {resultado}")
def raiz_quadrada(num1):
    resultado = math.sqrt(num1)
    operacao = 5
    resultado = salva_log(resultado, operacao, num1, 0)
    print(f"A raiz quadrada do numero {num1} é {resultado}")