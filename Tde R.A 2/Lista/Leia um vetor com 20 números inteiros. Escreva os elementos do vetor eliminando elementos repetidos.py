#Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos

tamanho = 20
vetor = []

for i in range(tamanho):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

elementos_unicos = set(vetor)

print("Elementos únicos:")
for elemento in elementos_unicos:
    print(elemento)

