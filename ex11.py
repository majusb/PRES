'''
Uma escola está realizando matrículas para um curso aberto à comunidade,
com limite de 20 vagas. Assumindo que os alunos são cadastrados por computador,
escreva um algoritmo que:
Leia a idade e o sexo do aluno;
Informe que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;
Mostre a idade média dos candidatos;
Mostre a quantidade de mulheres inscritas;
Mostre os candidatos (homens e mulheres) maiores de idade.

'''
idademedia=0.0
sexo=''
age=0
girls=0
maiores=0

for contador in range (0,20,1):
    age = int(input("Informe a idade: "))
    sexo = input("Digite F para feminino e M para masculino:")
    sexo=sexo.upper()
    if(sexo == 'F'):
        girls=girls+1
    else:
        print()
    if(age>=18):
        maiores=maiores+1
    idademedia+=age/20

print ("Turma lotada")
print(f"A quantidade de mulheres iscritas é {girls}")
print(f"A idade média é {idademedia:,.2f}")
print(f"Há {maiores} maiores de idade")
