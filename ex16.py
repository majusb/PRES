'''
Criar uma matriz 3x3 de números inteiros, solicite números para preencher essa matri e 
depois mostre a mesma na tela.


'''
m = [[0]*3, [0]*3, [0]*3]
linha =0
coluna=0

for linha in range (0,3,1):
    for coluna in range (0,3,1):
        m[linha][coluna] = int(input(f"Digite o número da posição ({linha},{coluna}):"))


for linha in range(0,3,1):
    for coluna in range(0,3,1):
        print(m[linha][coluna], end=" ")
    print()