import utilitarios
def jogo_velha():
    cont = 0
    xis = "×"
    ball = "O"
    jogo = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print('''
------JOGO DA VELHA------
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9   ''')
    for i in jogo:
        if jogo[0][0] == "x" and jogo[0][1] == "x" and jogo[0][2] == "x" or jogo[0][0] == "x" and jogo[1][0] == "x" and jogo[2][0] == "x" or jogo[0][0] == "x" and jogo[1][1] == "x" and jogo[2][2] == "x":
            print("vitoria do x")
        # se loko essa condicao enorme pra verificar somente uma casa da matriz