#Exercicio

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere
# produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda

import copy
from aula91_m import produtos

novos_produtos = [
    {**produto, 'preco' : round(produto['preco']*1.05,2)}
    for produto in produtos

]

produtos_ordem_decrescente = sorted(
    copy.deepcopy(produtos), 
    key=lambda produto: produto['nome'],
    reverse = True
)

produtos_ordem_preco = sorted(
    produtos,
    key=lambda produto:produto['preco']
)


print(novos_produtos)
print()
print(produtos_ordem_decrescente)
print()
print(produtos_ordem_preco)