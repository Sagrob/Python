def media(a,b,c,d):
    return (a+b+c+d)/4
while True:
    try:
        n1 = float(input("Insira a primeira nota: "))
        n2 = float(input("Insira a segunda nota: "))
        n3 = float(input("Insira a terceira nota: "))
        n4 = float(input("Insira a quarta nota: "))
    except:
        print("Por favor, digite um número")
        continue
    resultado = media(n1,n2,n3,n4)
    print("A média aritmética é", resultado)
    break
