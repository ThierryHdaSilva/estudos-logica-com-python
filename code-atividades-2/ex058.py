# Desafio: cifra de Cesar
# Desloque cada letra de uma mensagem para codificar um texto simples.


alfabeto = "abcdefghijklmnopqrstuvwxyz"


def codificar(mensagem, deslocamento):
    """Aplica a cifra de César e preserva maiúsculas e caracteres especiais."""
    resultado = ""

    for caractere in mensagem:
        letra = caractere.lower()
        if letra in alfabeto:
            nova_posicao = (alfabeto.index(letra) + deslocamento) % len(alfabeto)
            letra_codificada = alfabeto[nova_posicao]
            resultado += letra_codificada.upper() if caractere.isupper() else letra_codificada
        else:
            resultado += caractere

    return resultado


mensagem = input("Mensagem para codificar: ")

while True:
    try:
        deslocamento = int(input("Quantidade de posicoes para deslocar: "))
        break
    except ValueError:
        print("Digite um numero inteiro.")

print("Mensagem codificada:", codificar(mensagem, deslocamento))
