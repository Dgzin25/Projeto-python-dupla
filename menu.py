import os
import platform
#menu chamando todas funções
import calculadora
import verificador_senha
import gerador_de_senhas
# função de limpar o console
def limpa_tela():
    sistema = platform.system() # Pego o sistema que o usuario está usando
    if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
        os.system("cls")
    else:
        os.system("clear") # se não for windows ele executa esse comando para limpar o console
#----------------------------------------------------------
while True:
    print('''
    -------------BEM-VINDO AO MENU----------------
            Digite o numero desejado
    0 - para fechar o sistema
    1 - Calculadora
    2 - Verificador de senhas forte
    3 - Gerador de senhas
    ''')
    num = int(input("digite um numero de 1 a 3: "))
    if num == 0:
        limpa_tela()
        break
    elif num == 1:
        limpa_tela()
        calculadora.calculadora()
    elif num == 2:
        limpa_tela()
        verificador_senha.verificador_senha()
    elif num == 3:
        limpa_tela()
        gerador_de_senhas.gerador_de_senhas()