filmBatman = {
"title": "Batman",
"yearRelase": 2010,
"imdbRating": 8.8,
"genre": ["Sci-fi", "Action", "Thriller"]
}
print(filmBatman)
print(len(filmBatman))
print(type(filmBatman))

# 1- Recuerar um elemento do dicionario
print(filmBatman["genre"])
print(filmBatman.get("imdbRating"))

# 2-Buscar apenas as chaves do dicionario
print(filmBatman.keys())

# 3- Buscar apenas os valores do dicionario
print(filmBatman.values())

# 4- Buscar itens do dicionario com chave e valor
print(filmBatman.items())

# 5- Adicionar  no dicionario
filmBatman["director"] = "Christopher Nolan"
print(filmBatman)

# 6- Atualizar itens no dicionario
filmBatman.update({"imdbRating": 8.7})
print(filmBatman)

# 7- Remover item no dicionario
filmBatman.pop("director")
print(filmBatman)