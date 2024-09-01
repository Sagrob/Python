#uma cidade classifica um índice de poluição menor que 35 como agradável, de 35 até 60 desagradável e acima de 60 perigoso.
#escreva um algoritmo em python que leia um valor real(fracionado) representando o indice e imprime a classificação adequada pra ele

indice_p = float(input("Digite o índice de poluição: "))

if indice_p < 35:
    clas = "Agradável"
elif indice_p >= 35 and indice_p <= 60:
    clas = "Desagradável"
else:
    clas = "Perigoso"

print("O índice de poluição",indice_p, "é classificado como.", clas)
