#VARIAVEL GLOBAL

variavel_local = "Estou fora da funcao"
def funcao():
    # global permite acessar a variável externa; parâmetros costumam ser
    # uma alternativa mais fácil de testar.
    global variavel_local
    print(variavel_local)

funcao() #Vai imprimir: Estou fora da funcao
