##Faça um programa que receba do usuario um vetor com 10 posições. Em seguida devera ser impresso o maior e o menor elemento do vetor
#utilizando função

def encontrar_maior_menor(vetor):
    maior = vetor[0]
    menor = vetor[0]

    for elemento in vetor:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento

    return maior, menor


tamanho = 10
vetor = []

for i in range(tamanho):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

maior_elemento, menor_elemento = encontrar_maior_menor(vetor)

print("Maior elemento:", maior_elemento)
print("Menor elemento:", menor_elemento)


