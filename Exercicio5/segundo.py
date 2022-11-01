#um programa que leia um conjunto de nomes de 20 estudantes inscritos na prova do ENEM.
# Com esses nomes, realizar uma ordenação crescente
# uma função para facilitar a localização do nome na lista que será afixada no quadro de avisos da escola.

nomes = []

for k in range(0,20):#laco de 20 iteracoes

    nome = input("Insira o "+ str(k+1) +"º nome >>" )

nomes.append(nome)

nomes.sort()

print("==================")

print("Lista de nomes ordenados:")

for n in range(0,20):

    print(str(n+1)+ "º nome >> " + nomes[n])