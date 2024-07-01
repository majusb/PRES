num1=0
num2=0



def apresentacao(n1,n2):
    resposta= n1+n2
    return resposta

for i in range (0,1,1):
    num1= int(input(f"Digite o número {i+1}:"))
    num2 = int(input(f"Digite o número {i+2}:"))

print(apresentacao(num1,num2))
