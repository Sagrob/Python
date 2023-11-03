#Tarefa 1

def somar(num1, num2):
    resultado = num1 + num2
    return resultado


numero01 = int(input("Primeiro número: "))
numero02 = int(input("Segundo número: "))
numero03 = int(input("Terceiro número: "))
numero04 = int(input("Quarto número: "))
numero05 = int(input("Quinto número: "))
numero06 = int(input("Sexto número: "))
numero07 = int(input("Sétimo número: "))
numero08 = int(input("Oitavo número: "))
print()

print("O resultado do primeiro número com o segundo número foi: ", somar(numero01, numero02))
print("O resultado do terceiro número com o quarto número foi: ", somar(numero03, numero04))
print("A soma do quinto número com o sexto foi: ", somar(numero05, numero06))
print("A soma do setimo número com o oitavo foi: ", somar(numero07, numero08))
print()

#Tarefa 2

def somar(n1, n2, n3):
    resultado = n1 + n2 + n3
    return resultado

numero01 = int(input("Primeiro número: "))
numero02 = int(input("Segundo número: "))
numero03 = int(input("Terceiro número: "))
print("O resultado da soma foi: ", somar(numero01, numero02, numero03))
print()

#Tarefa 3

def exercicio_1(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


n = int(input('Digite um número: '))
exercicio_1(n)
print()

#Tarefa 4

def argu(n):
    if n > 0:
        print("P")
    elif n <= 0:
        print("N")

n = float(input("Digite um número: "))
argu(n)
print()

#Tarefa 5

def somaImposto(taxaImposto, custo):
    return (1+taxaImposto/100) * custo

custo = float(input("Digite o custo do produto: "))
taxaImposto = int(input("Digite a taxa do imposto: "))
print("valor com imposto: ", somaImposto(taxaImposto, custo))
print()
