#Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos
#utilizando função

def encontrar_elementos_unicos(vetor):
    elementos_unicos = set(vetor)
    return elementos_unicos


tamanho = 20
vetor = []

for i in range(tamanho):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

elementos_unicos = encontrar_elementos_unicos(vetor)

print("Elementos únicos:")
for elemento in elementos_unicos:
    print(elemento)

