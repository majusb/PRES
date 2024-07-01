'''
Construir um algoritmo que leia a idade de N pessoas.
O sistema deve calcular: a média das idades, a menor e a maior idade informada

'''
people=0
menori=0
maiori=0
contador=0
idade=0
idadesoma=0.0

people= int(input("Digite quantas pessoas vão participar: "))
for contador in range(1,people+1,1):
    idade= int(input(f"informe a idade da {contador}° pessoa:"))
    idadesoma+=idade/people 
    
    if(contador==0):
        maiori = idade
        menori = idade
    else:
        if(idade>maiori):
            maiori=idade
        else:
            if (idade<maiori):
                menori=idade
            else:
                print()
     
         


print(f"A média das idades é {idadesoma:,.2f}")
print(f"A maior idade é {maiori}")
print(f"A menor idade é {menori}")





