import pandas as pd
import pymongo

# Convertendo o arquivo CSV para JSON
df_man = pd.read_csv('./arquivos/worldcup_man.csv')
df_woman = pd.read_csv('./arquivos/worldcup_woman.csv')

json_man = df_man.to_json(orient='records')
json_woman = df_woman.to_json(orient='records')

# Salvar JSON em arquivos
with open('man.json', 'w') as man_file:
    man_file.write(json_man)

with open('woman.json', 'w') as woman_file:
    woman_file.write(json_woman)


# PERSISTINDO OS DADOS NO BD

# Criando a conexão
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Definindo os dados de conexão, onde o DB é a database, e as collections
db = client["Entrega2"]
colecao_man = db["wcp_man"]
colecao_woman = db["wcp_woman"]

# Carregando os dados JSON dos arquivos
with open('./arquivos/man.json', 'r') as man_file:
    dados_man = man_file.read()

with open('./arquivos/woman.json', 'r') as woman_file:
    dados_woman = woman_file.read()

# Convertendo os dados JSON em listas de dicionários para adicionar ao mongo
dados_man = eval(dados_man)
dados_woman = eval(dados_woman)

# Inserindo os dados JSON nas coleções
colecao_man.insert_many(dados_man)
colecao_woman.insert_many(dados_woman)

print("Dados inseridos com sucesso no MongoDB!")
