#menu chamando todas funções
import calculadora
import verificador_senha

while True:
    print('''
    -------------BEM-VINDO AO MENU----------------
            Digite o numero desejado
    0 - para fechar o sistema
    1 - Calculadora
    2 - Verificador de senhas forte
    ''')
    num = int(input("digite um numero de 1 a 2: "))
    if num == 0:
        break
    elif num == 1:
        calculadora.calculadora()
    elif num == 2:
        verificador_senha.verifcador_senha()