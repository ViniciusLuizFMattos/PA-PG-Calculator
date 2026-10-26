"""
PA & PG MD
Gerador e analisador de Progressões Aritméticas (PA) e Geométricas (PG).

Organização do arquivo:
    1. Planejamento (respostas da Etapa 1)
    2. Lógica das progressões (termo a termo, com laço)
    3. Versão em terminal (menu da Etapa 2)
    4. Testes e verificação matemática (Etapa 4)
    5. Front end (janela gráfica)  <- fica por último, como pedido
"""

import sys


# =============================================================================
# 1. PLANEJAMENTO
# =============================================================================
# 1) Para construir uma PA: primeiro termo, razão (r) e quantidade de termos.
# 2) Para construir uma PG: primeiro termo, razão (q) e quantidade de termos.
# 3) Próximo termo da PA: termo_atual + r
# 4) Próximo termo da PG: termo_atual * q
# 5) Soma: começa em 0 e, a cada termo gerado, soma = soma + termo.
#
# Pseudocódigo:
#   ler tipo (1 = PA, 2 = PG), primeiro termo, razão, quantidade
#   termo <- primeiro termo ; soma <- 0 ; lista <- vazia
#   repita 'quantidade' vezes:
#       guardar termo na lista
#       soma <- soma + termo
#       se PA: termo <- termo + razão
#       se PG: termo <- termo * razão
#   mostrar lista, último termo e soma

# =============================================================================
# 2. LÓGICA DAS PROGRESSÕES
# =============================================================================

def gerar_pa(primeiro, razao, quantidade):
    """Gera uma PA termo a termo. Retorna (termos, soma)."""
    termos = []
    soma = 0
    termo = primeiro
    for _ in range(quantidade):
        termos.append(termo)
        soma += termo
        termo += razao
    return termos, soma


def gerar_pg(primeiro, razao, quantidade):
    """Gera uma PG termo a termo. Retorna (termos, soma)."""
    termos = []
    soma = 0
    termo = primeiro
    for _ in range(quantidade):
        termos.append(termo)
        soma += termo
        termo *= razao
    return termos, soma


def formatar(numero):
    """Mostra 5.0 como '5' e 0.5 como '0.5'."""
    return f"{numero:.10g}"


def montar_resultado(tipo, primeiro, razao, quantidade):
    """Gera a progressão e devolve o texto pronto para exibir."""
    gerar = gerar_pa if tipo == 1 else gerar_pg
    termos, soma = gerar(primeiro, razao, quantidade)
    nome = "PA" if tipo == 1 else "PG"
    return (
        f"{nome} gerada:\n"
        f"{', '.join(formatar(t) for t in termos)}\n"
        f"Último termo: {formatar(termos[-1])}\n"
        f"Soma dos termos: {formatar(soma)}"
    )


def ler_numero(texto):
    """Converte texto em número, aceitando vírgula decimal."""
    return float(texto.replace(",", "."))


def ler_quantidade(texto):
    """Converte texto em inteiro positivo (erro se inválido)."""
    quantidade = int(texto)
    if quantidade < 1:
        raise ValueError("A quantidade deve ser pelo menos 1.")
    return quantidade