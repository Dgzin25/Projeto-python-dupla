# Estrutura caixa eletronico
import utilitarios
def atualiza_saldo(nome, senha, saldo_atualizado):
    arquivo = open("dados/banco_caixa_eletronico.txt","r")
    lista_final = []
    for linha in arquivo:
        linha = linha.strip("\n")
        linha = linha.split(";")
        if linha[0] == nome and linha[1] == senha:
            lista_final.append(f"{nome};{senha};{(saldo_atualizado)}\n")
        else:
            lista_final.append(f"{linha[0]};{linha[1]};{linha[2]}\n")
    arquivo.close()
    arquivo = open("dados/banco_caixa_eletronico.txt", "w")
    for i in lista_final:
        arquivo.write(i)
    arquivo.close()
    print(f"Olá {nome}, seu saldo foi atualizado para R$ {saldo_atualizado}")

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
#-------------------verificacao se o user esta cadastrado-----------------------------------
            nome = input("digite seu user: ")
            senha = input("digite sua senha: ")
            arquivo = open("dados/banco_caixa_eletronico.txt", "r")
            for linha in arquivo: #andando cada linha do arquivo
                linha = linha.strip("\n") #removendo os \n espacos
                linha = linha.split(";") #separando por ;
                if linha[0] == nome and linha[1] == senha:
                    saldo = int(linha[2])
                    print(f"Olá {nome} seu saldo é R$ {saldo}\n")
                    break
            arquivo.close()
#-------------------------------------------------------------------------------------------
            print(
"---------DIGITE SEU SAQUE OU DEPOSITO-------")
            num = int(input("Somente Numero inteiro positvo: "))
            num2 = num
            print(num)
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
1 - Sacar
2 - Depositar
3 - Fazer um novo deposito/saque
4 - Retornar ao menu''')      
                num1 = int(input("Digite o numero desejado: "))
                if num1 == 1:
                    if num2 > saldo:
                        utilitarios.limpa_tela()
                        print("Saldo insuficiente!!")
                        print(f"Seu saldo R${saldo}!!")
                        continue
                    else:
                        saldo_atualizado = saldo - num2
                        print(saldo_atualizado)
                        atualiza_saldo(nome, senha, saldo_atualizado)
                elif num1 == 2:
                    saldo_atualizado = saldo + num2
                    atualiza_saldo(nome, senha, saldo_atualizado)
                elif num1 == 3:
                    utilitarios.limpa_tela()
                    break
                elif num1 == 4:
                    utilitarios.limpa_tela()
                    return
                else:
                    utilitarios.limpa_tela()
                    print("digite um numero valido!!")