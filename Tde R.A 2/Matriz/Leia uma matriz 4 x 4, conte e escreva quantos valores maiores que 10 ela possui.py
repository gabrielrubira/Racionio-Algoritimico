#Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui


matriz = [[6, 7, 16, 15],
          [1, 2, 35, 50],
          [10, 11, 13, 22],
          [0, 5, 4, 6]]

contagem = 0 


for linha in matriz:
    for valor in linha:
        if valor > 10:
            contagem += 1

print("A matriz possui", contagem, "valores maiores que 10.")