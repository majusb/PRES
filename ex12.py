'''
Faça um algoritmo que solicite N números inteiros
até que o número 0(zero) seja digitado.
Ao final o algoritmo deve informar o maior e
o menor número digitado.
OBS: O número 0(zero) não pode ser contado.


'''
n=0
maior=0
menor=0

n=int(input("Digite um número:"))
maior=n
menor=n

while(n!=0):
    if(n>maior):
        manior=n
    else:
        if(n<menor):
           menor=n
    n=int(input("Digite um número:"))

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")



