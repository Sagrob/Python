while True:
    try:
        n1 = float(input("Insira a primeira nota: "))
        n2 = float(input("Insira a segunda nota: "))
        n3 = float(input("Insira a terceira nota: "))
        n4 = float(input("Insira a quarta nota: "))
    except:
        print("Por favor, digite um número")
        continue
    print("A média aritmética é", (n1 + n2 + n3 + n4)/4)
    break