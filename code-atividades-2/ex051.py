# Desafio: caixa eletronico
# Informe as cedulas necessarias para sacar um valor inteiro em reais.


def ler_valor():
    while True:
        try:
            valor = int(input("Valor do saque (somente reais inteiros): R$ "))
            if valor > 0:
                return valor
        except ValueError:
            pass

        print("Digite um valor inteiro maior que zero.")


valor = ler_valor()
valor_restante = valor
cedulas = [100, 50, 20, 10, 5, 2, 1]

print("Cedulas entregues:")
for cedula in cedulas:
    # divmod informa quantas cédulas cabem e qual valor ainda falta.
    quantidade, valor_restante = divmod(valor_restante, cedula)
    if quantidade:
        print(f"{quantidade} cedula(s) de R$ {cedula}")
