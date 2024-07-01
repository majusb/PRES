'''
Faça um algoritmo que inverta a posição dos valores
de um vetor de seis posições de inteiros. Ao final deve ser mostrado o
Vetor inicial e o final após as mudanças.
obs: só pode ser utilizado um vetor.


'''
vet=[0]*6



for i in range (0,6,1):
    vet[i] = int(input(f"Digite o valor do {i+1} vetor:"))
print("O valor inicial é ", end=" ")
for i in range(0,6,1):
    print (vet[i], end=" ")



print("O vetor invertido é ", end=" ")
for i in range (5,-1,-1):
    print(vet[i], end=" ")