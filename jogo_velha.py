import utilitarios
def jogo_velha():
    xis = "X"
    ball = "O"
    while True:
        jogo = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        print('''
------JOGO DA VELHA------
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9   ''')
        win = False
        empate = False
        cont = 0
        while True:
            num = int(input("Digite o numero da casa desejada: "))
            if num < 1 or num > 9:
                print("Entrada invalida")
                continue
            else:
                # N = COLUNAS DA MATRIZ
                # formula L = (NUM - 1) // N pega a divisao inteira
                # Formula C = (NUM - 1) % N, pega resto da divisao
                linha = (num-1)//3
                coluna = (num-1)%3 # pesquisei essa formula pois meu metodo ia repetir muitos if, eu ia numerar cada num com a devida casa da matriz
                if jogo[linha][coluna] == "X" or jogo[linha][coluna] == "O":
                    print("Casa ocupada!")
                    continue
                else:
                    if cont % 2 == 0:
                        jogo[linha][coluna] = xis
                        cont +=1
                        utilitarios.limpa_tela()
                    else:
                        utilitarios.limpa_tela()
                        jogo[linha][coluna] = ball
                        cont +=1
                    # verificacao  das linhas
                    if jogo[0][0] == jogo[0][1] == jogo[0][2] or jogo[1][0] == jogo[1][1] == jogo[1][2] or jogo[2][0] == jogo[2][1] == jogo[2][2]:
                        win = True
                        break
                    # verificacao das colunas
                    elif jogo[0][0] == jogo[1][0] == jogo[2][0] or jogo[0][1] == jogo[1][1] == jogo[2][1] or jogo[0][2] == jogo[1][2] == jogo[2][2]:
                        win = True
                        break
                    # verificacao das diagonais
                    elif jogo[0][0] == jogo[1][1] == jogo[2][2] or jogo[0][2] == jogo[1][1] == jogo[2][0]:
                        win = True
                        break
                if cont == 9 and win == False:
                    empate = True
                    break
                print(f'''
        ------JOGO DA VELHA------
            {jogo[0][0]} | {jogo[0][1]} | {jogo[0][2]}
            {jogo[1][0]} | {jogo[1][1]} | {jogo[1][2]}
            {jogo[2][0]} | {jogo[2][1]} | {jogo[2][2]}
            ''')
        if win == True or empate == True:
            if win:
                print(f'''
----------------------WIN--------------------
    {jogo[0][0]} | {jogo[0][1]} | {jogo[0][2]}
    {jogo[1][0]} | {jogo[1][1]} | {jogo[1][2]}
    {jogo[2][0]} | {jogo[2][1]} | {jogo[2][2]}
====================VITORIA=================''')
            else:
                print(f'''
----------------------DRAW--------------------
    {jogo[0][0]} | {jogo[0][1]} | {jogo[0][2]}
    {jogo[1][0]} | {jogo[1][1]} | {jogo[1][2]}
    {jogo[2][0]} | {jogo[2][1]} | {jogo[2][2]}
====================EMPATE=================''')
                
            while True:
                print('''
=====MENU======
1 - Jogar novamente
2 - Voltar para o menu''')
                num = int(input("Digite o numero desejado: "))
                if num == 1:
                    utilitarios.limpa_tela()
                    break
                elif num == 2:
                    utilitarios.limpa_tela()
                    return
                else:
                    utilitarios.limpa_tela()
                    print("Entrada Invalida!")
