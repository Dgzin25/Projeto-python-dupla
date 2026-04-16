#menu chamando todas funções
import utilitarios
import calculadora
import verificador_senha
import gerador_de_senhas
import caixa_eletronico
while True:
    print('''
    -------------BEM-VINDO AO MENU----------------
            Digite o numero desejado
    0 - para fechar o sistema
    1 - Calculadora
    2 - Verificador de senhas forte
    3 - Gerador de senhas
    4 - Caixa eletronico
    ''')
    num = int(input("digite um numero de 1 a 3: "))
    if num == 0:
        utilitarios.limpa_tela()
        break
    elif num == 1:
        utilitarios.limpa_tela()
        calculadora.calculadora()
    elif num == 2:
        utilitarios.limpa_tela()
        verificador_senha.verificador_senha()
    elif num == 3:
        utilitarios.limpa_tela()
        gerador_de_senhas.gerador_de_senhas()
    elif num == 4:
        utilitarios.limpa_tela()
        caixa_eletronico.caixa_eletronico()