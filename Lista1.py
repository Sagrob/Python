#Tarefa 1

print("Olá mundo")
print()
print()

#Tarefa 2

numero = (3)

print("O numero informado foi:", numero)
print()
print()

#Tarefa 3

numero01 = float(input("primeiro numero: "))
numero02 = float(input("segundo numero: "))
print(numero01 + numero02)
print()
print()

#Tarefa 4

primeira_nota = float(input("primeira nota: "))
segunda_nota = float(input("segunda nota : "))
terceira_nota = float(input("terceira nota: "))
quarta_nota = float(input("Quarta nota: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota)/4

print(media)
print()
print()

#Tarefa 5

metros = float(input("Quantos metros deseja converter: "))
print(metros*100)
print()
print()

#Tarefa 6

print("Tarefa 6")
print()
Raio_circulo = float(input("Insira o raio do círculo: "))
print(Raio_circulo**2*3.14)
print()
print()

#Tarefa 7

print("Tarefa 7")
print()
lado_quadrado = int(input("Insira o lado do quadradro: "))
print("Área total: ", lado_quadrado*4)
print("Dobro da Área: ", lado_quadrado*4*2)
print()
print()

#Tarefa 8

print("Tarefa 8")
print()
ganho_por_hora = float(input("Quanto você ganha por hora: "))
hora_por_mes = float(input("Quantas horas você trabalha no mês: "))
print(ganho_por_hora * hora_por_mes)
print()
print()

#Tarefa 9

print("Tarefa 9")
print()
fahrenheit = float(input("Insira quantos graus fahrenheit está: "))
print("Está", (fahrenheit-32)*5/9, "° Graus Celsius")
print()
print()

#Tarefa 10

print("Tarefa 10")
print()
Celsius = float(input("Insira quantos graus celsius está: "))
print("Está", (Celsius+32)/5*9, "° Graus Fahrenheit")
print()
print()

#Tarefa 11

print("Tarefa 11")
print()
primeiro_numero_inteiro = int(input("Insira um número inteiro: "))
segundo_numero_inteiro = int(input("Insira outro número inteiro: "))
terceiro_numero_real = float(input("Insira um número real: "))
print()
print("O produto do dobro do primeiro com metade do segundo: ", primeiro_numero_inteiro*2 + segundo_numero_inteiro/2)
print("A soma do triplo do primeiro com o terceiro: ", primeiro_numero_inteiro*3 + terceiro_numero_real)
print("O terceiro elevado ao cubo: ", terceiro_numero_real**3)
print()
print()

#Tarefa 12

print("Tarefa 12")
print()
altura = float(input("Insira sua altura: "))
print()
print("Peso ideal: ", altura * 72.7 - 58)
print()
print()

#Tarefa 13

print("Tarefa 13")
print()
altura = float(input("Insira sua altura: "))
print()
print("Peso ideal masculino: ", altura * 72.7 - 58)
print("Peso ideal feminino: ", altura * 62.1 - 44.7)
print()
print()

#Tarefa 14

print("Tarefa 14")
print()
peso = float(input("Insira o peso do peixe: "))
excesso = peso-50

if peso < 50:
    print("Não teve excesso de peso: ", peso)

elif peso == 50:
    print("Não teve excesso de peso: ", peso)

elif peso > 50:
    print("Excesso de peso do peixe: ", excesso)
    print("Multa a pagar: ", excesso*4 )
print()
print()

#Tarefa 15

print("Tarefa 15")
print()
ganho_por_hora = float(input("Quanto você ganha por hora: "))
hora_por_mes = float(input("Quantas horas você trabalha no mês: "))
salario_bruto = ganho_por_hora * hora_por_mes
imposto = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
salario_liquido = salario_bruto - imposto - inss - sindicato
print("Salário Bruto: ", salario_bruto, "R$")
print("Imposto de renda: ", imposto, "R$")
print("INSS: ", inss, "R$")
print("Sindicato: ", sindicato, "R$")
print("Salário Líquido: ", salario_liquido, "R$")
print()
print()

#Tarefa 16
#Faça um programa para uma loja de tintas(Pedir tamanho em metros quadrados da área a ser pintada, 1 litro para cada 3 metros quadrados,
#a tinta é vendida em latas de 18 litros que custam 80 reais, informe o preço total e a quantidade de latas de tintas a serem compradas
print("Tarefa 16")
print()
print("Bem vindo a loja de tintas!")
metros = float(input("Quantos metros quadrados deseja pintar?: "))
litros = metros / 3
latas = litros / 18
print("Litros totais: ", int(litros))
print("Quantidade de latas: ", int(latas))
print("Preço total: ", int(latas*80), "R$")
print()
print()


#Tarefa 17
print("Tarefa 17")
print()
print()