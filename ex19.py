'''
Faça um algoritmo que leia uma matriz 2 x 3 real
e depois imprima a matriz original e depois gere e
imprima sua matriz transposta (matriz 3 x 2 equivalente)

'''

mat=[[0]*3,[0]*3]
mat2=[[0]*2,[0]*2,[0]*2]

for i in range (0,2,1):
    for j in range (0,3,1):
        mat[i][j] = int(input(f"Digite o número da posição ({i}, {j}):"))

for i in range(0,2,1):
        for j in range( 0,3,1): 
            print (f"{mat[i][j]}", end=" ")
        print()

for i in range(0,3,1):
    for j in range(0,2,1):
        mat2[i][j]=mat[j][i]

for i in range(0,3,1):
    for j in range(0,2,1):        
        print(f"{mat2[i][j]}", end=" ")
    print()