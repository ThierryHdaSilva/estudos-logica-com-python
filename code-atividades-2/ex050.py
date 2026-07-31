# Desafio: palindromo
# Descubra se uma frase continua igual quando lida de tras para frente.


def normalizar(frase):
    """Remove espaços/sinais e padroniza letras para comparar o palíndromo."""
    return "".join(caractere.lower() for caractere in frase if caractere.isalnum())


frase = input("Digite uma palavra ou frase: ").strip()
frase_normalizada = normalizar(frase)

if not frase_normalizada:
    print("Nao foi informado nenhum caractere valido.")
elif frase_normalizada == frase_normalizada[::-1]:
    print("A frase e um palindromo.")
else:
    print("A frase nao e um palindromo.")
