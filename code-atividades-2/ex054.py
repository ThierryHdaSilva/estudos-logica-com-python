# Desafio: jogo da palavra secreta
# Tente descobrir a palavra antes de esgotar as seis tentativas erradas.


# A lista guarda cada letra correta apenas uma vez.
palavra_secreta = "python"
letras_descobertas = []
tentativas_erradas = 0
limite_de_erros = 6

while tentativas_erradas < limite_de_erros:
    exibicao = "".join(
        letra if letra in letras_descobertas else "_" for letra in palavra_secreta
    )
    print("Palavra:", " ".join(exibicao))

    if "_" not in exibicao:
        print("Parabens, voce descobriu a palavra!")
        break

    palpite = input("Digite uma letra: ").lower().strip()
    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas uma letra.")
    elif palpite in letras_descobertas:
        print("Essa letra ja foi descoberta.")
    elif palpite in palavra_secreta:
        letras_descobertas.append(palpite)
        print("Acertou!")
    else:
        tentativas_erradas += 1
        print(f"Errou. Restam {limite_de_erros - tentativas_erradas} tentativa(s).")
else:
    print(f"Fim de jogo. A palavra era: {palavra_secreta}.")
