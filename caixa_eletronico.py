# Estrutura caixa eletronico
import utilitarios
import time
import processa_caixa

def caixa_eletronico():
    usuarios = processa_caixa.atualiza_informacoes()
    while True:
#-------------------verificacao se o user esta cadastrado-----------------------------------
            nome = input("digite seu user: ")
            senha = input("digite sua senha: ")
            if nome in usuarios and usuarios[nome]["senha"] ==senha:
                None
            else:
                print("Dados invalidos!!")
                continue
#-------------------------------------------------------------------------------------------
            while True:
                cem = 0
                ciquenta = 0
                vinte = 0
                dez = 0
                cinco = 0
                dois = 0
                um = 0
                print(f'''
Olá {nome} seu saldo atual é {usuarios[nome]["saldo"]}
----------------------------------------                      
1 - Sacar
2 - Depositar
3 - LOGOUT
4 - Transferir 
5 - Retornar ao menu
---------------------------------------''')
                try:
                    num1 = int(input("Digite o numero desejado: "))
                except ValueError:
                    print("Entrada invalida somente numeros!!")
                if num1 == 3:
                    utilitarios.limpa_tela()
                    processa_caixa.atualiza_saldo(usuarios)
                    break
                if num1 > 5 or num1 < 1:
                    print("Numero invalido")
                    continue
                print(
"---------DIGITE VALOR DO SAQUE/DEPOSITO OU TRANSFERENCIA-------")
                try:
                    num = int(input("Somente Numero inteiro positvo: "))
                    valor = num
                except ValueError:
                    print("Somente numeros é permitido!")
                    continue
                match num1:
                    case 1:
                        if valor > usuarios[nome]["saldo"]:
                            utilitarios.limpa_tela()
                            print("SALDO INSUFICIENTE!!")
                            continue
                        else:
                            usuarios[nome]["saldo"] = usuarios[nome]["saldo"] - valor
                    case 2:
                        usuarios[nome]["saldo"] = usuarios[nome]["saldo"] + valor
                    case 4:
                        receptor = input("digite o nome do usuario que vai receber: ")
                        if receptor in usuarios and valor <= usuarios[nome]["saldo"]:
                            usuarios[receptor]["saldo"] = usuarios[receptor]["saldo"] + valor
                            usuarios[nome]["saldo"] = usuarios[nome]["saldo"] - valor
                            print("tranferencia feita com sucesso")
                        else:
                            print("Usuario não encontrado ou Saldo insuficiente")
                    case 5:
                        utilitarios.limpa_tela()
                        processa_caixa.atualiza_saldo(usuarios)
                        return
                    case _:
                        utilitarios.limpa_tela()
                        print("digite um numero valido!!")
#--------------------------------------------------------------------------------                 
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
---ARGUARDE 5 SEGUNDOS---
        ''')
                time.sleep(5)
caixa_eletronico()  