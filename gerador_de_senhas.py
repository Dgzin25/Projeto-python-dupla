import random
import time
import utilitarios


# ---------------- Estrutura Principal ---------------
def gerador_de_senhas():
    while True:
        print('''
-----MENU-SENHAS-----
0 - para retornar
1 - Senha simples
2 - Senha forte
        ''')
        num = int(input("digite o numero desejado: "))
        if num == 0:
            utilitarios.limpa_tela()
            return
        elif num == 1:
            utilitarios.limpa_tela()
            senha_simples()
        elif num == 2:
            utilitarios.limpa_tela()
            senha_forte()
        else:
            utilitarios.limpa_tela()
            print("Digite um numero valido")
            continue
# ----------------Gerador de Senha simples somente 8 caracteres e um numero------------
def senha_simples():
    letras = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
             "d", "f", "g", "h", "j", "k", "l", "ç", "z", "x", "c", "v", "b", "n", "m"]
    senha = []
    for i in range(6):
        aleatorio = random.choice(letras)
        senha.append(aleatorio)
    for i in range(2):
        aleatorio = random.randint(0, 9)
        senha.append(str(aleatorio)) # str transforma o numero em string
    senha_final = "".join(senha) # junta tudo em uma string, as "" serve como separador metodo
    print(f''' 
Senha Simples:
----------------
    {senha_final}
-----------------
Retornando ao menu de senhas em 5 segundos
          ''')
    time.sleep(5)
    utilitarios.limpa_tela()
# ---Gerador de Senha Forte 9 caracteres, numero, letra maiuscula, minuscula, caractere especial
def senha_forte():
    letras = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
             "d", "f", "g", "h", "j", "k", "l", "ç", "z", "x", "c", "v", "b", "n", "m"]
    caracteres = ["!", "@", "$", "%", "&",]
    senha = []
    for i in range(6):
        aleatorio = random.choice(letras)
        senha.append(aleatorio)
    j = random.randint(0, 5) #sorteando qual letra vai ficar maiusculo
    senha[j] = senha[j].upper() # aplicando a letra
    for i in range(2):
        aleatorio = random.randint(0, 9)
        senha.append(str(aleatorio))
    aleatorio = random.choice(caracteres)
    senha.append(str(aleatorio))
    senha_final = "".join(senha)
    print(f''' 
Senha Forte:
----------------
    {senha_final}
-----------------
Retornando ao menu de senhas em 5 segundos
          ''')
    time.sleep(5)
    utilitarios.limpa_tela()
# possivel upgrade pra personalizar senha o usuario digita o tamanho da senha, 
# se quer incluir numeros, caracteres, letras maiuscula