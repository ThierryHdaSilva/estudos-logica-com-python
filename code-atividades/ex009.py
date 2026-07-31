# Desenvolva um programa que realize a validação de dados.
# O script deve ler o sexo de uma pessoa, mas só aceitar os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor válido.

# Estrutura de repetição while: repete até receber M ou F.
while True:
    sexo = input("Informe o sexo (M/F): ").strip().upper()
    if sexo in ("M", "F"):
        print(f"Valor aceito: {sexo}")
        break
    print("Valor inválido. Digite apenas M ou F.")
