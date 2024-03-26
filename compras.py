compras = []

produtos = [
    {"id": 1, "descricao": "Celular", "preco": 15000 }
    ,{"id": 2, "descricao": "computador", "preco": 3000}
    ,{"id": 3, "descricao": "roteador", "preco": 100}
]
client = {}

print("escolha um produto")
for i in range(len(produtos)):
    print(produtos[i])