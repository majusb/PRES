'''
Criar um algoritmo que leia 5 números pelo
teclado e exiba os números na ordem inversa da
que os números foram digitados.


'''
vet=[0]*5



for i in range (0,5,1):
    vet[i]=input("Digite um número:") 
print("Sequencia de:",end=" ")
for i in range (0,5,1):
     print(vet[i], end=" ")
print()
print("Ao contrário fica:", end=" ")
for i in range (4,-1,-1):
    print(vet[i], end=" ")
