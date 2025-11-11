filmsList = ["Batman", "Superman", "One Piece", "Naruto", "Pulp Fiction"]

# 1- Tamanho da lista
print(len(filmsList))

# 2- Recuperar um item da lista pelo nome
print(filmsList.index("Naruto"))

# 3- Adicionar item ao final da lista
filmsList.append("The Lord of Rings")
print(filmsList)

# 4- Ordenada a lista
filmsList.sort()
print(filmsList)

# 5- Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsList.remove("Pulp Fiction")
print(filmsCopy)

# 6- Remove todos os itens da lista
filmsList.clear()
print(filmsList)