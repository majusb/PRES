'''
Construa um algoritmo que determine quanto será gasto para encher o
tanque de um carro. O usuário fornecerá os seguintes dados: Tipo de
carro (TC) (G – gasolina ou A – álcool) e Capacidade do tanque (CT),
em litros. Após a escolha do tipo de veículo e da capacidade do tanque,
o sistema irá imprimir uma mensagem falando o tipo do carro(
Gasolina ou álcool) e pedirá para o usuário informar o
valor do preço do litro do combustível.
Como saída, será informado para o usuário, o valor,
em reais, do preço de se encher tanque de combustível.

'''
tanque=0.0
carro=""
gas=0.0
total=0.0

print("CALCULO DO GASTO DE UM CARRO")
print("Selecio ne o tipo se carro:")
carro = input("Digite G: gasolina ou A: para álcool: ")
tanque = float(input("Digite o tamanho do tanque do carro: "))
carro = carro.upper()

if(carro == "G"):
    carro= "DE GASOLINA"
else:
    carro= "DE ÁLCOOL"

print(f"O carro selecionado foi {carro}, que tem a capacidade de {tanque} litros")
gas=float(input(f"Informe o valor do litro de {carro}: "))
total=gas*tanque
print(f"O valor ficará em {total} abastecido {carro}")   
