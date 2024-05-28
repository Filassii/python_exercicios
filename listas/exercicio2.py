numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
print("Lista de números:", numeros)
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
media = soma / len(numeros)
print("Soma de todos os números:", soma)
print("Maior número da lista:", maior)
print("Menor número da lista:", menor)
print("Média dos números da lista:", media)