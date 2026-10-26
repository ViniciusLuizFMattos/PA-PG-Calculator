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
