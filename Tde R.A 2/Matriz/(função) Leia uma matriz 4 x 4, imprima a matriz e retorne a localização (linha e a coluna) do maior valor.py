#Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor


def encontrar_maior_valor(matriz):
    maior_valor = float('-inf')
    linha_maior_valor = -1
    coluna_maior_valor = -1

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_maior_valor = i
                coluna_maior_valor = j

    return linha_maior_valor, coluna_maior_valor

matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição ({i + 1}, {j + 1}): "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(' '.join(str(valor) for valor in linha))

linha_maior, coluna_maior = encontrar_maior_valor(matriz)
print(f"O maior valor é {matriz[linha_maior][coluna_maior]} e está na linha {linha_maior + 1}, coluna {coluna_maior + 1}.")

