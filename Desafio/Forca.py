import random


print("***************************")
print('Bem-Vindo ao jogo da Forca!')
print("***************************")

palavras = ["campo", "bola", 'gol', 'trave', "comemoração"]

palavra_para_adivinhar = random.choice(palavras)
letras_adivinhadas = ['-'] * len(palavra_para_adivinhar)


max_tentativas = 11
letras_erradas = []

while True:
    print('Palavra', ' '.join(letras_adivinhadas))
    print('Letras Erradas:', " ".join(letras_erradas))

    letras = input('Digite uma letra: ' ).lower()

    if letras in letras_adivinhadas or letras in letras_erradas:
        print('voce ja digitou essa letra. Tente denovo.')
        continue   

    if letras in palavra_para_adivinhar:
        for i in range(len(palavra_para_adivinhar)):
            if palavra_para_adivinhar[i] == letras:
                letras_adivinhadas[i] = letras
    else:
        letras_erradas.append(letras)
        
        
        if len(letras_erradas) == max_tentativas:
            print ("Perdeu! A palavra era: ", palavra_para_adivinhar)
            break


    if "-" not in letras_adivinhadas:
        print("Ganhou! Parabens!")
        break 