# Escrevendo em um arquivo.
from pathlib import Path

nome = input('Qual é o seu nome?').strip()
mensagem = f"Olá, {nome}!\n"

# O caminho é relativo ao próprio exercício, não à pasta de onde ele foi
# executado. Assim, o arquivo funciona mesmo quando chamado por outra pasta.
arquivo_saida = Path(__file__).with_name('saudacao.txt')
arquivo_saida.write_text(mensagem, encoding='utf-8')
print(f"Mensagem gravada em {arquivo_saida.name}: {mensagem.strip()}")

