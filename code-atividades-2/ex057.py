# Desafio: matriz 3 por 3
# Leia uma matriz e mostre as somas das linhas, colunas e diagonal principal.


def ler_linha(numero_da_linha):
    """Lê exatamente três inteiros para uma linha da matriz."""
    while True:
        try:
            linha = [int(numero) for numero in input(
                f"Linha {numero_da_linha} (3 numeros separados por espaco): "
            ).split()]
            if len(linha) == 3:
                return linha
        except ValueError:
            pass

        print("Digite exatamente tres numeros inteiros.")


matriz = [ler_linha(indice) for indice in range(1, 4)]

# enumerate fornece o número da linha e a própria lista de valores.
for indice, linha in enumerate(matriz, start=1):
    print(f"Soma da linha {indice}: {sum(linha)}")

for coluna in range(3):
    soma_coluna = sum(matriz[linha][coluna] for linha in range(3))
    print(f"Soma da coluna {coluna + 1}: {soma_coluna}")

diagonal = sum(matriz[indice][indice] for indice in range(3))
print(f"Soma da diagonal principal: {diagonal}")
