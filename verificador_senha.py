import string
import os
import platform
# Estrutura verificador de senhas
def verificador_senha():
    sistema = platform.system() # Pego o sistema que o usuario está usando
    while True:
        print('''
========Bem-vindo========       
Verificador de senha forte!!
=========================''')
        senha = input("Digite a senha: ")
        Isupper = False
        Islower = False
        Isnumeri = False
        tem_especial = False
        caracteres_especial = string.punctuation # puxo uma lista de caracteres especiais da biblioteca string
        for i in senha:
            if i.isupper():
                    Isupper = True
            if i.islower():
                    Islower = True
            if i.isnumeric():
                    Isnumeri = True
            if i in caracteres_especial: # verifico se a senha existe na lista de caracteres
                    tem_especial = True
        if Isupper and Islower and Isnumeri and tem_especial and len(senha) >= 8:
            if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
                os.system("cls")
            else:
                os.system("clear") # se não for windows ele executa esse comando para limpar o console
            print(f"sua senha {senha} é forte!!")
        else:
            if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
                os.system("cls")
            else:
                os.system("clear")
            print("SENHA FRACA!!")
#----------MENU DE RETORNO-----------------
        while True:   
            print('''
--------SENHA VERIFICADA COM SUCESSO!!------------
1 - Verificar uma nova senha
2 - Retornar ao menu''')
            num = int(input("digite o numero desejado: "))
            if num == 1:
                if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
                     os.system("cls")
                else:
                     os.system("clear")
                break
            elif num == 2:
                if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
                    os.system("cls")
                else:
                    os.system("clear") 
                return
            else:
                if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
                     os.system("cls")
                else:
                     os.system("clear")
                print("\nDIGITE UM NUMERO VALIDO!!")
                continue
verificador_senha()