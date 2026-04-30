import utilitarios
import processa_caixa
def cadastro_caixa():
    usuario = processa_caixa.atualiza_informacoes()
    while True:
        deposito = 0
        print("BEM-VINDO AO CADASTRO!!")
        nome = input("digite seu usuario: ").lower()
        senha = input("digite sua senha: ")
        try:
            deposito = float(input("Deposito Inicial/opcional: "))
        except ValueError: # tratando erro de entrada com string
            print("Entrada invalida, somente numeros no deposito")
            continue
        if deposito.is_integer(): # verifico se o numero é inteiro
            deposito = int(deposito)
        if nome in usuario:
            print("Usuario ja cadastrado!!")
            continue
        else:
            usuario[nome] = {"senha": senha, "saldo": deposito}
            print("USUARIO CADASTRADO COM SUCESSO!!") 
        while True:
            print('''
-----------MENU-----------
1 - Cadastrar um novo usuario!
2 - Voltar ao menu!''')
            try:
                num1 = int(input("digite o numero desejado: "))
            except ValueError:
                print("Letras não são permitido, Somente numeros inteiro")
                continue
            match num1:
                case 1:
                    utilitarios.limpa_tela()
                    processa_caixa.atualiza_saldo(usuario)
                    break
                case 2:
                    utilitarios.limpa_tela()
                    processa_caixa.atualiza_saldo(usuario)
                    return
                case _:
                    print("Numero entra 1 e 2!!")
                    continue
cadastro_caixa()