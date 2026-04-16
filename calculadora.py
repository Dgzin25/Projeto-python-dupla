#estrutura da calculadora

def calculadora():
    while True:
        print('''
            ======MENU======
        0 - para retornar ao menu       
        1 - Soma
        2 - subtrair
        3 - Multiplicar
        4 - Divisão
        ''')
        num = int(input("digite um numero da operção: "))
        if num == 0:
            return
        if num == 1:
            soma()

#-------------Funções das operações--------------
def soma():
    num1 = float(input("digite um numero: "))