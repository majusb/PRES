'''
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o 
percentual de lucro do distribuidor e dos impostos ao preço de fábrica. Faça
um programa que receba o preço de fábrica de um veículo, o percentual de lucro
do distribuidor e o percentual de impostos.
 Calcule e mostre:
    a) o valor correspondente ao lucro do distribuidor;
    b) o valor correspondente ao imposto;
    c) o preço final de veículo

'''
carro=0.0
imposto=0.0 
lucro=0.0
newcar=0.0

print("Esse programa calcula o preço final de um veículo")
carro = float(input("Digite o valor do carro:"))
imposto = float(input("Digite o valor do imposto:"))
lucro = float(input("Digite o valor do lucro:"))

newcar= carro + (imposto/100*carro) + (lucro/100*carro)

print(f"O preço final do veículo é`{newcar}")
print(f"O lucro do distribuidor é {lucro/100*carro}")
print(f"O valor do imposto é {imposto/100*carro}")
