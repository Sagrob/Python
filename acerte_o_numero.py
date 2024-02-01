import random
while True:
    numero = random.randint(1,10)
    jogar = int(input("1-Quero jogar\n0-Quero sair\n"))
    if jogar == 0:
       break

    if jogar > 1:
        print("Por favor, digite um número válido!")
        print()
        continue
    elif jogar < 0:
        print("Por favor, digite um número válido!")
        print()
        continue

    try:
        numeroJ = int(input("Insira um número de 1 a 10: "))
    except:
        print("Por favor, digite um número válido!")
        print()
        continue

    if numeroJ < 1:
        print("Número menor que o esperado!")
        print()
        continue
    elif numeroJ > 10:
        print("Número maior que o esperado!")
        print()
        continue

    if numeroJ == numero:
        print("Você venceu")    
        break
    else:
        print("Você perdeu. \nO número era",numero)
        print()
        continue
