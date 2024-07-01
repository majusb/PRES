'''
Escrever um algoritmo que leia os dados de N pessoas
(nome, sexo(M/F), idade e saúde(B/R)) e informe
se está apta ou não para cumprir o serviço militar obrigatório.
Informe os totais de aptos e não aptos no final do algoritmo.
Se o candidato estiver apto deve ser mostrado o seu nome e a mensagem que está apto.
Para estar apto o candidato deve possuir 18 anos,
ser do sexo masculino e estar com a saúde boa.
Caso o candidato não possa servir deve ser mostrado o seu nome e o motivo.
O sistema deve ficar solitando dados até que seja digitado N.


'''

nome=""
sexo=""
saude=""
idade=0
apt=0
napt=0
vezes=""

nome=input("Digite seu nome:")
sexo=input("Digite F- feminino M-masculino")
idade=input("Digite sua idade:")
saude=input("Como está sua saúde B-boa ou R-ruim:")

while(vezes != 'N'):
    if(idade>=18):
        apt=apt+1



print(f"{nome}, você está apto para o serviço militar")
print(f"{nome}, você não está apito para o serviço militar por causa de:")
print(f"{sexo}")
print(idade)
