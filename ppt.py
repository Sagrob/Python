#só um pedra, papel e tesoura normal!
import random
while True:

    operacao = input("Qual deseja jogar?\n 1-Pedra \n 2-Papel \n 3-Tesoura \n 0-Sair \n ")
    if int(operacao) == 0:
            break
    
    adversario = random.randint(1,3)
    
    if adversario == 1:
        adversario_jogada = "Pedra"
    elif adversario == 2:
        adversario_jogada = "Papel"
    else:
        adversario_jogada = "Tesoura"

    if operacao == '1':
        print(f"O adversario escolheu: {adversario_jogada}")
        if adversario == 1:
            print("Empate")
            break
        elif adversario == 2:
            print("Você perdeu")
            break
        else:
            print("Você ganhou")
            break
        
    if operacao == '2':
        print(f"O adversario escolheu: {adversario_jogada}")
        if adversario == 1:
            print("Você ganhou")
            break
        elif adversario == 2:
            print("Empate")
            break
        else:
            print("Você perdeu")
            break
    
    elif operacao == '3':
        print(f"O adversario escolheu: {adversario_jogada}")
        if adversario == 1:
            print("Você perdeu")
            break
        elif adversario == 2:
            print("Você ganhou")
            break
        else:
            print("Empate")
            break

    else:
        print("Escolha uma das opções! \n")
