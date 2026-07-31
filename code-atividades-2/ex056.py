# Desafio: alerta de estoque
# Leia produtos no formato produto:quantidade e indique os que precisam ser repostos.


def ler_estoque():
    """Converte texto no formato produto:quantidade em um dicionário."""
    while True:
        entrada = input("Produtos (ex.: arroz:4, feijao:1): ").strip()
        estoque = {}

        try:
            for item in entrada.split(","):
                produto, quantidade = item.split(":")
                produto = produto.strip()
                quantidade = int(quantidade.strip())
                if not produto or quantidade < 0:
                    raise ValueError
                estoque[produto] = quantidade
            return estoque
        except ValueError:
            print("Use o formato produto:quantidade, com quantidades nao negativas.")


estoque = ler_estoque()

while True:
    try:
        minimo = int(input("Estoque minimo desejado: "))
        if minimo >= 0:
            break
    except ValueError:
        pass
    print("Digite um numero inteiro nao negativo.")

produtos_para_repor = [
    # O estoque precisa ser menor que o mínimo, não apenas igual a ele.
    produto for produto, quantidade in estoque.items() if quantidade < minimo
]

if produtos_para_repor:
    print("Produtos que precisam ser repostos:")
    for produto in produtos_para_repor:
        print(f"- {produto}: {estoque[produto]} unidade(s)")
else:
    print("Todos os produtos estao com estoque suficiente.")
