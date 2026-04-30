#menu chamando todas funções
import utilitarios
import calculadora
import verificador_senha
import gerador_de_senhas
import caixa_eletronico
import jogo_velha
import cadastro_caixa
while True:
    print('''
    -------------BEM-VINDO AO MENU----------------
            Digite o numero desejado
    0 - para fechar o sistema
    1 - Calculadora
    2 - Verificador de senhas forte
    3 - Gerador de senhas
    4 - Caixa eletronico
    5 - Cadastrar no caixa eletronico
    6 - jogo da velha
    ''')
    try:
        num = int(input("digite um numero de 1 a 5: "))
    except ValueError:
        print("somente numeros inteiros!")
        continue
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
    elif num == 5:
        utilitarios.limpa_tela()
        cadastro_caixa.cadastro_caixa()
    elif num == 6:
        utilitarios.limpa_tela()
        jogo_velha.jogo_velha()