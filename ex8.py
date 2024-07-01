'''
Faça um programa que receba o salário de um funcionário,
calcule e mostre o novo salário desse funcionário,
acrescido de bonificação e de auxílio escola.
Salário                               Bonificação
Até R$ 500,00                         5%
Entre R$ 500,00 e R$ 1200,00          12%
Acima de R$ 1200,00                   0%

Salário                        Auxílio Escola
Até R$ 600,00                  R$150,00
Mais que 600,00                R$ 100,00

'''
sal=0.0
salf=0.0
salb=0.0

sal = float(input("Informe seu salário: "))
if(sal<= 500):
    salf= (sal*5/100)+sal
else:
    if (sal>500 and sal <= 1200):
            salf= (sal*12/100)+sal
    else:
        if(sal > 1200):
                salf=sal
        else:
                 print() 
if(sal<=600):
    salb = salf+150
else:
    if(sal>600):
        salb=salf+100
    else:
        print()
print (f"O salário final é de {salb} reais.")
                            



