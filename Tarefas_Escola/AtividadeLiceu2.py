def media(a,b,c):
    return (a+b+c)/3
def soma(a,b,c):
    return a+b+c

while True:
    try:
        operacao = int(input(" 1-Media Aritmetica \n 2-Soma \n 3-É par? \n 0-Sair \n Qual operação deseja: "))
    except:
        print("Por favor, digite um número válido!")
        print()
        continue
    if int(operacao) == 0:
        break
        
    if int(operacao) not in [1,2,3]:
        print('Escreva um número válido!')
        continue

    primeiro_numero = int(input("Primeiro numero: ")) 
    resultado = primeiro_numero%2
    if int(operacao) == 3:
        if resultado == 0:
            print("O número",primeiro_numero,"é par.")
            break
        else:
            print("O número",primeiro_numero,"é ímpar.")
            break

    segundo_numero = int(input("Segundo numero: "))
    terceiro_numero = int(input("Terceiro numero: "))

    if int(operacao) == 1:
        resultado = media(primeiro_numero, segundo_numero, terceiro_numero)
        print('A média aritmetica é', resultado)
        break
    if int(operacao) == 2:
        resultado = soma(primeiro_numero, segundo_numero, terceiro_numero)
        print('A soma é', resultado)
        break
