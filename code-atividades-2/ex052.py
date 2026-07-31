# Desafio: resumo de temperaturas
# Analise temperaturas registradas durante alguns dias.


def ler_temperaturas():
    """Lê pelo menos duas temperaturas em uma única linha."""
    while True:
        entrada = input("Temperaturas separadas por virgula: ").strip()
        try:
            temperaturas = [float(valor.strip()) for valor in entrada.split(",")]
        except ValueError:
            print("Digite numeros validos, separados por virgula.")
            continue

        if len(temperaturas) < 2:
            print("Informe pelo menos duas temperaturas.")
            continue

        return temperaturas


# As funções sum, max e min resumem a lista sem precisar de um laço manual.
temperaturas = ler_temperaturas()
media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print(f"Media: {media:.1f} C")
print(f"Maior temperatura: {maior:.1f} C")
print(f"Menor temperatura: {menor:.1f} C")
print(f"Amplitude termica: {maior - menor:.1f} C")
