'''
exercício de fazer uma tabuada

'''
tab=0
tabuada=0
res=0


tab = int(input("Digite um número para a tabuada:"))

for tabuada in range (1,11,1):
    res=tab*tabuada
    print(f"{tab} * {tabuada} = {res}")