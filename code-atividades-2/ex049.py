# Desafio: maior sequencia crescente
# Receba uma lista de numeros e mostre a maior sequencia de valores
# estritamente crescentes que aparecem lado a lado.


def ler_numeros():
    """Lê uma lista com pelo menos dois números inteiros."""
    while True:
        entrada = input("Digite numeros inteiros separados por virgula: ").strip()

        try:
            numeros = [int(numero.strip()) for numero in entrada.split(",")]
        except ValueError:
            print("Entrada invalida. Use somente numeros inteiros separados por virgula.")
            continue

        if len(numeros) < 2:
            print("Digite pelo menos dois numeros.")
            continue

        return numeros


def maior_sequencia_crescente(numeros):
    """Retorna a maior sequência estritamente crescente e consecutiva."""
    maior_sequencia = [numeros[0]]
    sequencia_atual = [numeros[0]]

    for numero in numeros[1:]:
        if numero > sequencia_atual[-1]:
            sequencia_atual.append(numero)
        else:
            if len(sequencia_atual) > len(maior_sequencia):
                maior_sequencia = sequencia_atual
            sequencia_atual = [numero]

    if len(sequencia_atual) > len(maior_sequencia):
        maior_sequencia = sequencia_atual

    return maior_sequencia


numeros = ler_numeros()
sequencia = maior_sequencia_crescente(numeros)

print(f"Maior sequencia crescente: {sequencia}")
print(f"Quantidade de elementos: {len(sequencia)}")
