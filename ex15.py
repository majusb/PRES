'''
Faça um algoritmo que leia 5 números reais em um vetor e depois
mostre os números localizados nas posições impares.


'''

vet=[0]*5
i=0

for i in range (0,5,1):
    vet[i]=input("Digite um valor:")
for i in range (0,5,1):   
    if((i % 2) !=0):
        print(vet[i])