# Desafio: pares que atingem uma meta
# Encontre os pares de numeros cuja soma e igual a um valor escolhido.


def ler_inteiros(mensagem):
    """Lê números inteiros separados por vírgula."""
    while True:
        try:
            return [int(numero.strip()) for numero in input(mensagem).split(",")]
        except ValueError:
            print("Digite somente numeros inteiros separados por virgula.")


numeros = ler_inteiros("Numeros inteiros separados por virgula: ")

while True:
    try:
        meta = int(input("Soma desejada: "))
        break
    except ValueError:
        print("Digite uma soma inteira valida.")

vistos = set()
pares = set()
for numero in numeros:
    # Para cada número, procuramos anteriormente o seu complemento até a meta.
    complemento = meta - numero
    if complemento in vistos:
        pares.add(tuple(sorted((complemento, numero))))
    vistos.add(numero)

if pares:
    print("Pares encontrados:")
    for primeiro, segundo in sorted(pares):
        print(f"{primeiro} + {segundo} = {meta}")
else:
    print("Nenhum par encontrou a soma desejada.")
