# Lista de produtos, cada um representado por um dicionário
produtos = [
    {'nome': 'Produto 1', 'preco': 50},
    {'nome': 'Produto 2', 'preco': 60},
    {'nome': 'Produto 3', 'preco': 75},
    {'nome': 'Produto 4', 'preco': 120},
    {'nome': 'Produto 5', 'preco': 30}
]

print("Lista de Produtos:")
for produto in produtos:
    print(f"{produto['nome']} - {produto['preco']} R$")