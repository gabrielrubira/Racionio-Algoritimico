#Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida 
#utilizando função

def criar_matriz_diagonal(valor_diagonal):
    matriz = [[0] * 5 for _ in range(5)]

    for i in range(5):
        matriz[i][i] = valor_diagonal

    return matriz

matriz = criar_matriz_diagonal(7)

for linha in matriz:
    print(linha)

