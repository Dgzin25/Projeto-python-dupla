# Estrutura caixa eletronico
import utilitarios
def caixa_eletronico():
    while True:
        cem = 0
        ciquenta = 0
        vinte = 0
        dez = 0
        cinco = 0
        dois = 0
        um = 0
        while True:
            print("---------DIGITE SEU SAQUE OU DEPOSITO-------")
            num = int(input("Somente Numero inteiro positvo: "))
            if num < 0:
                utilitarios.limpa_tela()
                print("SOMENTE VALORES POSITIVOS!!")
                continue
            while True:
                if num == 0:
                    break
                elif num >= 100:
                    cem += 1
                    num -= 100
                elif num >= 50 and num < 100:
                    ciquenta += 1
                    num -= 50
                elif num >= 20 and num < 50:
                    vinte += 1
                    num -= 20
                elif num >= 10 and num < 20:
                    dez += 1
                    num -= 10
                elif num >= 5 and num < 10:
                    cinco += 1
                    num -= 5
                elif num >= 2 and num < 5:
                    dois += 1
                    num -= 2
                else:
                    um += 1
                    num -= 1
            print(f'''
======SAQUE/DEPOSITO=====
{cem} notas de 100!
{ciquenta} notas de 50!
{vinte} notas de 20!
{dez} notas de 10!
{cinco} notas de 5!
{dois} notas de 2!
{um} moedas de 1!
========================
    ''')  
            while True:
                print('''
1 - Fazer um novo deposito/saque
2 - Retornar ao menu''')      
                num1 = int(input("Digite o numero desejado: "))
                if num1 == 1:
                    utilitarios.limpa_tela()
                    break
                elif num1 == 2:
                    utilitarios.limpa_tela()
                    return
                else:
                    utilitarios.limpa_tela()
                    print("digite um numero valido!!")

''''Upgrade simples que deixaria o caixa eletrônico nível “banco real”

Adicionar saldo:

Exemplo:

saldo = 1000

Depois:

if saque > saldo:
    print("Saldo insuficiente")

E atualizar:

saldo -= saque'''