import json

# Função para criar um dicionário com base nos argumentos
def criar_json(nome_empresa, ano_fundacao, categorias_produto, endereco, produtos):
    servicos_venda_online = {
        "nome_empresa": nome_empresa,
        "ano_fundacao": ano_fundacao,
        "categorias_produto": categorias_produto,
        "endereco": endereco,
        "produtos": produtos
    }
    return servicos_venda_online

# Argumentos para criar o JSON
nome_empresa = "Hippogriff"
ano_fundacao = 2021
categorias_produto = ["Eletronicos", "Moda Esportiva"]
endereco = {
    "rua": "Facisa",
    "cidade": "Campina Grande",
    "estado": "PB",
    "CEP": "12345-678"
}
produtos = [
    {
        "nome": "Camisa Flamengo",
        "preco": 349.90,
        "estoque": 300,
        "desconto": None
    },
    {
        "nome": "PS5",
        "preco": 3599.99,
        "estoque": 72,
        "desconto": {
            "percentual": 10,
            "validade": "2023-12-31"
        }
    }
]

# Criar o JSON com base nos argumentos
json_data = criar_json(nome_empresa, ano_fundacao, categorias_produto, endereco, produtos)

# Converter os dados para formato JSON
json_string = json.dumps(json_data, indent=4)

# Exibir o JSON criado
print(json_string)

# Salvar o JSON em um arquivo (opcional)
with open("Q11.json", "w") as json_file:
    json_file.write(json_string)
