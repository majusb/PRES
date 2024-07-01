'''
Desenvolver um algoritmo que solicite o nome e a
idade de um nadador e imprima na tela o seu nome,
a sua idade e em qual categoria ele está.
    idade                 categoria
    5 a 7                 Infantil A
    8 a 11                Infantil B
    12 a 13               Juvenil A
    14 a 17               Juvenil B
    18 a >                Adulto
Caso seja digitado uma idade fora das classes acima,
informar que o nadador não possui uma categoria válida.


'''
nome=""
idade=0

nome = input("Digite o nome:")
idade = int (input ("Digite a idade: "))

if(idade>=5 and idade <=7):
    print(f"{nome}, com idade de {idade} esta na Categoria Infantil A")
else:
    if(idade>=8 and idade<=11):
        print(f"{nome}, com idade de {idade} esta na Categoria Infantil B")
    else:
        if(idade >= 12 and idade<=13):
            print(f"{nome}, com idade de {idade} esta na Juvenil A")
        else:
            if(idade>=14 and idade<=17):
                print(f"{nome}, com idade de {idade} esta na Juvenil B")
            else:
                if(idade>=18):
                    print(f"{nome}, com idade de {idade} esta na Adulto")
                else:
                    print(f"nadador {nome} com {idade} anos não possui uma categoria válida")