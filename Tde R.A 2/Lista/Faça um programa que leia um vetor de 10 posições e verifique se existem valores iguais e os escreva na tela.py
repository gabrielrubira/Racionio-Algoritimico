#Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
#Função que não recebe parâmetro de entrada e possue retorno

def encontrar_valores_iguais():
    tamanho = 10
    lista = []
    for i in range(tamanho):
        valor = int(input("Digite um valor inteiro: "))
        lista.append(valor)

    valores_iguais = []
    for i in range(tamanho):
        if lista.count(lista[i]) > 1 and lista[i] not in valores_iguais:
            valores_iguais.append(lista[i])

    return valores_iguais


valores_iguais = encontrar_valores_iguais()

if len(valores_iguais) > 0:
    print("Valores iguais foram encontrados:")
    for valor in valores_iguais:
        print(valor)
else:
    print("Não foram encontrados valores iguais!")
