def atualiza_informacoes():
    usuarios = {}
    arquivo = open("dados/banco_caixa_eletronico.txt", "r")
    for linha in arquivo:
        linha = linha.strip("\n")
        linha = linha.split(";")
        usuarios[linha[0]] = {"senha": linha[1], "saldo": float(linha[2]) } 
    arquivo.close()
    return(usuarios)
def atualiza_saldo(usuarios):
    arquivo = open("dados/banco_caixa_eletronico.txt","w")
    for nome in usuarios:
        if usuarios[nome]["saldo"].is_integer():
            (usuarios[nome]["saldo"]) = int(usuarios[nome]["saldo"])
        arquivo.write(f"{nome};{usuarios[nome]["senha"]};{usuarios[nome]["saldo"]}\n")
    arquivo.close()