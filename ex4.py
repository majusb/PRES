'''
Faça um algoritmo que receba o nome e duas notas de um aluno.
Calcule a média e ao final mostre o nome do aluno, a média e a sua situação.
Caso a média seja no mínimo 6, o aluno está aprovado, se a média for inferior a 6 e 
no mínimo 4 o aluno está de Exame e se a média for inferior a 4 o mesmo está reprovado.

'''

aluno=""
p1=0.0
p2=0.0
media=0.0
situacao=""

print("Calculo da média do aluno")
aluno = input("Digite o nome do aluno: ")
p1 = float(input("Digite a nota da primeira prova: "))
p2 = float (input ("Digite a nota da segunda prova: "))

media = (p1 + p2)/2
if(media>=6):
    situacao = "APROVADO"
else:
    if(media<4):
        situacao = "REPROVADO"
    else:
        situacao = " EM RECUPERAÇÂO"

print(f"Aluno: {aluno}")
print(f"está {situacao} com a média de {media}")
