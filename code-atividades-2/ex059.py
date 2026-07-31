# Desafio: medidor de forca de senha
# Avalie uma senha usando tamanho, letras maiusculas, numeros e simbolos.


def avaliar_senha(senha):
    pontos = 0

    if len(senha) >= 8:
        pontos += 1
    if any(letra.islower() for letra in senha):
        pontos += 1
    if any(letra.isupper() for letra in senha):
        pontos += 1
    if any(letra.isdigit() for letra in senha):
        pontos += 1
    if any(not letra.isalnum() for letra in senha):
        pontos += 1

    if pontos <= 2:
        return "fraca"
    if pontos <= 4:
        return "media"
    return "forte"


senha = input("Digite uma senha para avaliar: ")

if not senha:
    print("A senha nao pode ficar vazia.")
else:
    print(f"A senha foi classificada como: {avaliar_senha(senha)}.")
