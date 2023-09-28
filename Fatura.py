while True:
    try:
        nomeCliente = str(input("Digite o nome do cliente: "))
        diaVencimento = int(input("Digite o dia de vencimento: "))
        mesVencimento = int(input("Digite o mês de vencimento: "))
        valorFatura = float(input("Digite o valor da fatura: "))
    except:
        print("Digite um caractere válido!")
        continue
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print("Olá,", nomeCliente)
    print("A sua fatura com vencimento em", diaVencimento,"de", meses[mesVencimento - 1],"no valor de R$",valorFatura,"está fechada.")
    break