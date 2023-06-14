#utilizando função
#Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui


def contar_valores_maiores_que_10(matriz):
    contagem = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contagem += 1
    return contagem

matriz = [[6, 13, 9, 16],
          [10, 7, 12, 5],
          [15, 3, 8, 11],
          [14, 4, 2, 17]]

quantidade = contar_valores_maiores_que_10(matriz)

print("A matriz possui", quantidade, "valores maiores que 10.")
