while True:
    try:
        venda = float(input("Qual o valor da venda?"))
        desconto = float(input("Qual a porcentagem do desconto?"))
    except:
        print("Por favor, digite um número")
        continue
resultado = (desconto / venda)*100
print("O valor com desconto será: ", resultado)
break