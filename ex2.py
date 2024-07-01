'''
Faça um programa que receba uma medida em pés.
Faça as conversões a seguir em mostre os resultados.
    a) polegadas
    b) jardas
    c) milhas
Sabese que:
    1 pé = 12 polegadas
    1 jarda = 3 pés
    1 milha = 1760 jardas

'''
pol=0.0
pes=0.0
j=0.0
m=0.0



print("Esse programa converte pés em:")
print("a) polegadas")
print("b) jardas")
print("C) milhas")


pes = float(input("Quantos pés serão?"))
pol = pes * 12
j = pes / 3
m = j / 1760

print(f"{pes} pés é igual a {pol} polegadas")
print(f"{pes} pés é igual a {j:,.2f} jardas")
print(f"{pes} pés é igual a {m:,.5f} milhas")


