import os
import platform

# função de limpar o console
def limpa_tela():
    sistema = platform.system() # Pego o sistema que o usuario está usando
    if sistema == "Windows": # verifico se o sistema dele é = ao windows, se for ele limpa o console
        os.system("cls")
    else:
        os.system("clear") # se não for windows ele executa esse comando para limpar o console
#----------------------------------------------------------