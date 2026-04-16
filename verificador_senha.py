import string
import utilitarios
#Estrutura verificador de senhas
def verificador_senha():
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
            utilitarios.limpa_tela()
            print(f"sua senha {senha} é forte!!")
        else:
            utilitarios.limpa_tela()
            print("SENHA FRACA!!")
#----------MENU DE RETORNO-----------------
        while True:   
            print('''
--------SENHA VERIFICADA COM SUCESSO!!------------
1 - Verificar uma nova senha
2 - Retornar ao menu''')
            num = int(input("digite o numero desejado: "))
            if num == 1:
                utilitarios.limpa_tela()
                break
            elif num == 2:
                utilitarios.limpa_tela()
                return
            else:
                utilitarios.limpa_tela()
                print("\nDIGITE UM NUMERO VALIDO!!")
                continue