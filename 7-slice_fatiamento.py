movieName = "Top Gun"
# String[inicio:fim] - indice começa na posição 0 | indice final -1

# 1- Busca toda String a partir da preimeira posição
print(movieName[0:])

# 2- Busca toda string até a ultima posição
print(movieName[:7])

# 3- Busca toda string da terceira até a ultima posição
print(movieName[2:])

"""
string[inicio:fim:passo]
indice começa na posição 0 | indice final - 1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5- Buscar toda a string nos indices impares
print(movieName[1::2])

# 5- Inverter uma string de trás para frente
print(movieName[::-1])