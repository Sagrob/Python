print("D1")
# Escreva um programa que solicita ao usuário um número inteiro positivo N e calcula a soma de todos os números pares de 1 a N.
n = int(input("Digite um número inteiro: "))
soma = 0
for i in range(2, n+1, 2):
    soma += 1
print(soma, "\n")



print("D2")
# Crie um programa que realize uma contagem regressiva a partir de um número inteiro informado pelo usuário até 1.
n = int(input("Digite um número: "))
from time import sleep
for contagem in range(n,0,-1):
    print(contagem)
    sleep(1)
print("Acabou seu Tempo!!!", "\n")



print("D3")
# Peça ao usuário para inserir notas de alunos e calcule a média das notas. O programa deve continuar pedindo notas até que o usuário decida parar.
quantidade = int(input("Insira a quantidade de notas: "))
abuabu = []
for x in range(quantidade):
    c = int(input("Digite a nota: "))
    abuabu.append(c)
soma_das_notas = sum(abuabu)
print(soma_das_notas/quantidade, "\n")



print("D4")
# Crie um programa que solicita ao usuário um número e verifica se ele está presente em um vetor predefinido.
l = {5}
n = int(input("Acerte o número de 1 a 10: "))
if n in l:
    print("Acertou!", "\n")
else:
    print("Errou!", "\n")



print("D5")
# Escreva um programa que calcula e exibe a tabuada de um número escolhido pelo usuário.
tabuada = int(input("Tabuada do número: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))