# PA & PG MD

Gerador e analisador de **Progressões Aritméticas (PA)** e **Progressões Geométricas (PG)** em Python.

Projeto 1 da disciplina de **Matemática Discreta** — UTFPR.

O objetivo é relacionar os conceitos matemáticos estudados com o **Pensamento Computacional**, transformando padrões matemáticos em algoritmos.

## O que o programa faz

Dados o **primeiro termo**, a **razão** e a **quantidade de termos**, o programa gera a sequência, mostra o último termo e calcula a soma de todos os termos.

Exemplo (PA com a₁ = 5, r = 3, n = 6):

```
PA gerada:
5, 8, 11, 14, 17, 20
Último termo: 20
Soma dos termos: 75
```

## Como funciona

A sequência é construída **termo a termo**, com um laço `for`, sem usar as fórmulas prontas do termo geral ou da soma:

```python
for _ in range(quantidade):
    termos.append(termo)   # guarda o termo atual
    soma += termo          # acumula a soma
    if tipo == 1:
        termo += razao     # PA: próximo = atual + r
    else:
        termo *= razao     # PG: próximo = atual * q
```

As fórmulas prontas só aparecem na parte de testes, para **conferir** o resultado do laço:

| | Termo geral | Soma |
|---|---|---|
| **PA** | aₙ = a₁ + (n − 1)·r | Sₙ = (a₁ + aₙ)·n / 2 |
| **PG** | aₙ = a₁·qⁿ⁻¹ | Sₙ = a₁·(qⁿ − 1) / (q − 1) |

## Estrutura do código

O arquivo `pa_pg.py` é dividido em 5 seções:

1. **Planejamento** — respostas da Etapa 1 e pseudocódigo (comentários).
2. **Lógica das progressões** — `gerar`, `formatar`, `montar_resultado` e leitura das entradas.
3. **Versão em terminal** — menu em texto, como no enunciado.
4. **Testes e verificação matemática** — 4 casos conferidos com as fórmulas.
5. **Front end** — janela gráfica (`tkinter`) com visual de folha de caderno.

## Como executar

Requer **Python 3** (o `tkinter` já vem com o Python no Windows).

Janela gráfica:

```bash
python pa_pg.py
```

Versão em terminal:

```bash
python pa_pg.py --terminal
```

Também há um executável para Windows (`.exe`) que abre a janela direto, sem precisar ter o Python instalado.

Para gerar o executável você mesmo:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed pa_pg.py
```

## Testes realizados

O botão **testes** da janela executa os quatro casos abaixo e compara o resultado do programa com as fórmulas.

| Teste | a₁ | Razão | n | Sequência | Soma | Verificação |
|---|---|---|---|---|---|---|
| PA crescente | 5 | 3 | 6 | 5, 8, 11, 14, 17, 20 | 75 | Correto |
| PA decrescente | 20 | −4 | 6 | 20, 16, 12, 8, 4, 0 | 60 | Correto |
| PG crescente | 2 | 3 | 5 | 2, 6, 18, 54, 162 | 242 | Correto |
| PG decrescente | 64 | 0,5 | 6 | 64, 32, 16, 8, 4, 2 | 126 | Correto |

Exemplo de conferência (PA decrescente): a₆ = 20 + 5·(−4) = 0 e S₆ = (20 + 0)·6 / 2 = 60 — igual ao valor calculado pelo laço.

## Autor

Vinicius Luiz — Ciência de Dados e Inteligência Artificial, UTFPR.
