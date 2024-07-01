'''
Faça um algoritmo que receba três notas de um aluno como parâmetros
e o tipo da média que deverá ser calculada.
Se o tipo da média for "A" a função calcula a média aritmética das
notas do aluno, se for "P" a função calcula a média ponderada
pesos 5, 3 e 2. A média calculada deve ser devolvida ao programa
principal para, então, ser mostrada.


'''

def mediaA(n1,n2,n3):
    mediaaf=(n1+n2+n3)/3
    return mediaaf

def mediaP(n1,n2,n3):
    mediapf=((n1*5)+(n2*3)+(n3*2))/10
    return mediapf

p1=0.0
p2=0.0
p3=0.0
tipo=""
quant=0

quant=int(input("Digite quantas médias serão calculadas:"))

for i in range(0,quant,1):
    print("Calculo da média escolar:")
    p1=float(input("Digite a nota da Prova 1:"))
    p2=float(input("Digite a nota da Prova 2:"))
    p3=float(input("Digite a nota da Prova 3:"))
    tipo=input("Qual será a média A-aritmética ou P-ponderada:")
    tipo=tipo.upper()
    if(tipo=='A'):
        print("A média final foi de ", end=" ")
        print(mediaA(p1,p2,p3))
    else:
        if(tipo == 'P'):
            print("A média final foi de ", end=" ")
            print(mediaP(p1,p2,p3))
        else:
            print()


