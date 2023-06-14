##Crie um programa utilizando vetor que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
#utilizando função

def ler_valores(tamanho):
    valores = []
    for i in range(tamanho):
        valor = int(input("Digite um valor que seja um número inteiro: "))
        valores.append(valor)
    return valores


tamanho = 6
valores = ler_valores(tamanho)

print("Valores:")
for valor in valores:
    print(valor)
