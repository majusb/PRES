'''
Você está fazendo um trabalho de classificação de solo. Após colher uma
amostra e verificar a quantidade de pontos de água presente nela, classificou
a amostra em:
    Rochosa: se menos ou igual a 10 pontos de água
    Firme: se mais do 10 e menos ou igual a 40 pontos
    Pantanosa: se mais do 40 e menos ou igual a 80 pontos
    Quantidade Inválida: se mais do que 80 pontos

'''
pa=0.0

print("CLASSIFICADOR DE TIPOS DE SOLO")
pa= float(input("Digite a quantidade de pontos de água: "))

if(pa<=10):
    print("SOLO ROCHOSO")
else:
    if(pa>10 and pa<=40):
        print("SOLO FIRME")
    else:
        if(pa>40 and pa<=80):
            print("SOLO PANTANOSO")
        else:
            print("QUANTIDADE INVÁLIDA")