# programa para ler o nome do carro o custo de fábrica de um carro.
# calcular e mostrar o nome do carro e o custo final ao consumidor.
# perguntar se deseja repetir e fazer de outro carro.
#o percentual do distribuidor seja de 28% e os impostos de 45%
continuar = 'S'
while continuar == 'S':

    valor = 60000
    distribuidor = 28/100
    imposto = 45 / 100

    nome = input("Digite o nome do carro : ");

    print("O valor do carro de fabrica é:",valor)

    print("valor ditribuido do carro é:",distribuidor * 0.28)

    print("valor do imposto do carro é:",imposto * 0.45)

    preco =(valor + distribuidor)

    print("Aplicando impostos e percentual do distribuidor, o preço deste veículo será de:",+preco )

    continuar = input("voce deseja continuar? s ou n:").upper()





