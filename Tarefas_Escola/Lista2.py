#Lista 2

#Tarefa 1

print("Irei imprimir o maior valor que colocar.")
print()
valor1 = float(input("Insira um valor: "))
valor2 = float(input("Insira outro valor: "))
print()

if valor1 > valor2:
    print("Seu maior valor é", valor1)

elif valor1 == valor2:
    print("Não existe maior valor.")

elif valor1 < valor2:
    print("Seu maior valor é", valor2)   
print()
print()

#Tarefa 2

print("Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo")
print()
numero = int(input("Insira um número: "))
if numero > 0:
    print("Seu número é positivo.")

elif numero == 0:
    print("Seu número é neutro.")

elif numero < 0:
    print("Seu número é negativo.")

print()
print()

#Tarefa 3

print('Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever. F - Feminino, M - Masculino, Sexo Inválido.')
print()
sexo = input("Insira F para feminino ou M para masculino: ").lower()

print()
if sexo == 'm' or sexo == "masculino":
    print("M-Masculino")

elif sexo == 'f' or sexo == "feminino":
    print("F-Feminino")

else:
    print("Sexo Inválido")
print()
print()

#Tarefa 4

print("Faça um Programa que verifique se uma letra digitada é vogal ou consoante")
print()
vogal = str(input("Insira uma letra para saber se é uma vogal ou consoante: ")).lower()

if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
    print("Vogal")

else:
    print("consoante")
