'''
Faça um programa que receba o salário base de um funcionário.
Calcule e mostre o salário a receber, sabendo que esse funcionário tem gratificação
de R$ 50,00 e paga imposto de 10% sobre o salário base.

'''
sal=0.0
salf=0.0

print("Esse programa calcula o salário a receber")
sal=float(input("Qual é o valor do seu salário:"))
salf=(sal*0.90)+50
print(f"O valor que irá receber levando em cosideração sua gratificação e o imposto é {salf}")