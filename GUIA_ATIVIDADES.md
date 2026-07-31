# Guia comentado das atividades

Este arquivo resume o objetivo, a lógica principal e os conceitos praticados em
cada exercício. Os comentários dentro dos arquivos mostram o detalhe local;
este guia ajuda a enxergar a sequência de aprendizagem.

## `code-atividades`

### Fundamentos, entrada e saída

- **`ex001.py`** — cria variáveis de texto e número, altera `xp` por meio de uma nova atribuição e exibe os dados do personagem. Pratica tipos `str` e `int`.
- **`ex002.py`** — soma dois inteiros e usa `type()` para descobrir o tipo de diferentes valores.
- **`ex003.py`** — lê dois números e calcula antecessor, sucessor, dobro, triplo, raiz quadrada e média. A raiz é validada para evitar um cálculo real inválido com número negativo.
- **`ex004.py`** — calcula média ponderada de quatro notas. Os dois primeiros bimestres pesam 2 e os dois últimos pesam 3; depois classifica o aluno como aprovado, recuperação ou reprovado.
- **`ex005.py`** — demonstra códigos ANSI para mudar a cor do texto no terminal.
- **`ex039.py`** — demonstra `input()` e f-string para personalizar uma mensagem.

### Repetição e condições

- **`ex006.py`** — calcula a média de oito notas usando `for`, acumulador (`soma`) e contador fixo.
- **`ex007.py`** — faz a mesma média com `range(1, 9)`. O limite final de `range` não é incluído, por isso o laço lê os alunos 1 a 8.
- **`ex008.py`** — repete a leitura com `while`; a variável `quantidade` controla quando o laço deve terminar.
- **`ex009.py`** — valida sexo até receber `M` ou `F`. `strip()` remove espaços e `upper()` permite aceitar letras minúsculas.
- **`ex010.py`** — percorre a palavra `rato` e monta a palavra invertida colocando cada novo caractere antes do resultado anterior.
- **`ex011.py`** — gera confrontos entre times. O fatiamento a partir do próximo índice evita confrontos duplicados e partidas contra o próprio time.
- **`ex012.py` e `ex015.py`** — aplicam três vezes a transformação `a = a * 2 - 3`, mostrando contador, condição e atualização de um `while`.
- **`ex013.py`** — imprime o valor 5 uma vez. O incremento foi incluído para que a condição do `while` deixe de ser verdadeira e não produza um loop infinito.
- **`ex014.py`** — conta divisores de um inteiro positivo. Se houver exatamente dois, o número é primo.

### Caixa eletrônico e estruturas de dados

- **`ex016.py`** — simula um saque usando as cédulas disponíveis, começando pela maior cédula escolhida. `//` calcula a quantidade e `%`/subtração mantém o restante.
- **`ex017.py`** — compara tupla e lista. A lista é alterada com atribuição, `append`, `sort` e `insert`, e `len()` conta seus elementos.
- **`ex018.py`** — cria uma lista e usa `enumerate()` para mostrar índice e valor.
- **`ex019.py`** — lê cinco valores para uma lista e percorre a lista com índice e conteúdo.
- **`ex20.py`** — cria uma cópia superficial com `a[:]`; alterar `b` não altera `a` nesse caso.
- **`ex21.py`** — transforma uma lista de listas em uma lista simples usando dois laços aninhados.
- **`ex22.py`** — mostra que `append()` modifica a lista original e retorna `None`; por isso o retorno não deve ser salvo em outra variável.
- **`ex23.py`** — soma números pares e subtrai números ímpares usando o operador resto `%`.
- **`ex24.py`** — usa um dicionário de frutas, acrescentando a chave `uvas` depois da criação.
- **`ex25.py`** — percorre chave e valor de um dicionário com `.items()` e soma/subtrai conforme a paridade do valor.
- **`ex26.py`** — usa fatiamento `[1:4]`, que começa no índice 1 e termina antes do índice 4.
- **`ex27.py`** — consulta um jogador pela posição informada e valida se o número está entre 1 e 15.

### Programa de compras

- **`ex28.py`** — cadastra produtos como dicionários dentro de uma lista, permite excluir itens e calcula o total da compra. Há laços separados para cadastro, exclusão e resumo.
- **`ex29.py`** — implementa a mesma ideia em uma versão mais compacta. `copy()` é importante para guardar uma fotografia de cada produto antes de reutilizar o dicionário temporário.

### Funções, módulos e arquivos

- **`ex30.py`** — apresenta escopo local: a variável criada dentro de `funcao()` só existe ali.
- **`ex31.py`** — apresenta escopo global e o uso de `global`; na prática, passar valores como parâmetros costuma ser mais seguro.
- **`ex32.py`** — define e chama uma função sem parâmetros.
- **`ex33.py`** — recebe dois parâmetros e devolve o resultado com `return`.
- **`ex34.py`** — reatribui um número dentro da função; o inteiro externo permanece 10 porque a reatribuição local não altera a variável original.
- **`ex35.py`** — altera uma lista dentro da função; como listas são mutáveis, a alteração aparece também fora dela.
- **`ex36.py`** — importa `datetime` e mostra a data atual do computador.
- **`ex37.py`** — faz uma requisição HTTP com `requests`, timeout e tratamento de erro de rede; depende de conexão e da biblioteca instalada.
- **`ex38.py`** — é um esqueleto de configuração de pacote para o `setuptools`, não um exercício de execução interativa.
- **`calcArea.py`** — reúne as fórmulas de área em funções reutilizáveis e rejeita medidas negativas.
- **`main.py`** — apresenta o menu, lê a opção, coleta as medidas e chama as funções de `calcArea.py`. O bloco `if __name__ == "__main__"` impede a execução automática quando o módulo é importado.
- **`ex040.py`** — grava uma saudação em `saudacao.txt` usando `pathlib` e UTF-8.
- **`041.py`** — lê o arquivo produzido por `ex040.py` e informa quando ele ainda não existe.
- **`ex042.py` e `ex043.py`** — calculam fatorial com `math.factorial`, validando números negativos antes da chamada.
- **`ex044.py`** — encapsula a validação de mês em uma função e lança `ValueError` para valores fora de 1 a 12.
- **`ex045.py`** — demonstra função interna: `interno()` é criada dentro de `externo()` e usada imediatamente.
- **`ex46.py`** — calcula a quantidade de notas de 50, 20 e 10 reais, recusando valores fora do limite ou impossíveis de montar.
- **`ex48.py`** — cria uma função simples que converte texto para minúsculas.
- **`ex41.py`** — compara dois valores e informa qual é maior ou se são iguais.

## `code-atividades-2`

- **`ex049.py`** — separa a leitura da solução e encontra a maior sequência estritamente crescente de valores consecutivos.
- **`ex050.py`** — normaliza uma palavra/frase removendo espaços e pontuação, então compara o texto com sua versão invertida para detectar palíndromos.
- **`ex051.py`** — valida um saque positivo e usa `divmod()` para decompor o valor nas cédulas de 100 a 1 real.
- **`ex052.py`** — lê temperaturas e calcula média, maior, menor e amplitude térmica.
- **`ex053.py`** — converte horários `HH:MM` em minutos desde meia-noite e calcula a duração de um evento no mesmo dia.
- **`ex054.py`** — implementa uma forca simples: mostra letras descobertas, controla tentativas erradas e encerra ao completar a palavra.
- **`ex055.py`** — encontra pares cuja soma bate com uma meta. O conjunto `vistos` torna a busca eficiente e `pares` elimina duplicatas.
- **`ex056.py`** — transforma itens `produto:quantidade` em dicionário e lista produtos abaixo do estoque mínimo.
- **`ex057.py`** — lê uma matriz 3x3 e calcula somas das linhas, colunas e diagonal principal.
- **`ex058.py`** — aplica cifra de César, usando módulo para voltar ao início do alfabeto e preservando maiúsculas e símbolos.
- **`ex059.py`** — pontua uma senha por tamanho, minúsculas, maiúsculas, números e símbolos, classificando-a em fraca, média ou forte.

## Como estudar e executar

Comece pelos exercícios numerados em ordem, observando sempre três partes: entrada
de dados, transformação e saída. Para testar um arquivo interativo, execute-o na
pasta correspondente, por exemplo:

```text
python code-atividades/main.py
python code-atividades/ex040.py
python code-atividades/041.py
python code-atividades-2/ex058.py
```

Execute `ex040.py` antes de `041.py`, pois o segundo depende do arquivo de texto
criado pelo primeiro.
