#Lista 3
#Tarefa 1

while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
    except:
        print("Por favor, digite um número")
        continue
    if nota < 0:
            print("valor inválido!")
    elif nota > 10:
            print("valor inválido!")
    else:
        nota == ''
        print("valor VÁLIDO!")
        break

print()
print()

#Tarefa 2

while True:
    nome_do_usuario = input("Digite o nome do usuário: ")
    senha_do_usuario = input("Digite a senha do usuário: ")

    if nome_do_usuario == senha_do_usuario:
        print("erro, por favor tente novamente!")
    else:
         print("Login efetuado com sucesso!")
         break
print()
print()    
#Tarefa 3

#while True:
#     nome = input("Digite seu nome: ")
#     if len(nome) <= 3:
#        print("Tente novamente.", nome, " menor que 3 caracteres")
#        continue
     
#Tarefa 4

ano = 0
pais_a = 80000
pais_b = 200000
crescimento_de_a = 1.03
crescimento_de_b = 1.015

while True:
     ano += 1
     pais_a *= crescimento_de_a
     pais_b *= crescimento_de_b

     if pais_a >= pais_b:
          print("país A chegou na popilação maior ou igual à B em ", ano)
          break
