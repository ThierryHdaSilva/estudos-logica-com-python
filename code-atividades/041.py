# Lendo de um arquivo.
from pathlib import Path

arquivo_entrada = Path(__file__).with_name('saudacao.txt')

try:
    conteudo = arquivo_entrada.read_text(encoding='utf-8')
    print(conteudo, end='')
except FileNotFoundError:
    print("Arquivo não encontrado. Execute ex040.py primeiro.")
