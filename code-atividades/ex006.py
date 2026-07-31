#Estruturas de Repetições
#Atividades de fixação
#Desenvolva um programa que faça uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# O laço evita repetir manualmente a leitura das oito notas.
soma = 0
quantidade_alunos = 8
for aluno in range(1, quantidade_alunos + 1):
    nota = float(input(f'Nota do aluno {aluno}: '))
    soma += nota

media = soma / quantidade_alunos
print('A media da turma foi {}'.format(round(media)))
