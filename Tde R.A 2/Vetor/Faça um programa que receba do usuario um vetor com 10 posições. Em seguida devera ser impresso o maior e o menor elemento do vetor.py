#Faça um programa que receba do usuario um vetor com 10 posições. Em seguida devera ser impresso o maior e o menor elemento do vetor


tamanho = 10
vetor = []

for i in range(tamanho):
    numero = int(input("Digite um numero inteiro: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for elemento in vetor:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento



print("Maior elemento: ", maior)
print("Menor elemento: ", menor)
