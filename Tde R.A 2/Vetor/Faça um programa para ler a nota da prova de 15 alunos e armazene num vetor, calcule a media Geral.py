#Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral

tamanho = 15

notas = []


for i in range(tamanho):
    nota = float(input("Digite a nota: "))
    if nota > 10:
        print("Essa nota é invalida!")
        nota = float(input("Digite a nota novamente: "))
    notas.append(nota)


soma = sum(notas)
média = soma / tamanho


print("Média Geral: ", média)





