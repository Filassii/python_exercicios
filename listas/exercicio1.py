# Criar a lista chamada "numeros", que contém os números de 1 a 10
numeros = list(range(1, 11))

# Criar a lista chamada "dobro", que contém o dobro de cada número da lista anterior
dobro = [numero * 2 for numero in numeros]

# Imprimindo as duas listas
print("Lista normal:", numeros)
print("Lista dobrada:", dobro)