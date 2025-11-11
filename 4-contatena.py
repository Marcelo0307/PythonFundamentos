name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("===================")
# Alternativa 1
print("Nome do filme:",name)
print("Ano do Lançamento:",yearLaunch)
print("Nota do Filme",noteMovie)

# Alternativa 2
print("Nome do filme:", name,"\nAno do Lançamento:", yearLaunch,"\nNota do Filme:", noteMovie)

# Alternativa 3 """F String"""
print(f"Nome do jogo: {name}\n"
      f"Ano do Lançamento: {yearLaunch}\n"
      f"Nota do Filme: {noteMovie}\n"
)