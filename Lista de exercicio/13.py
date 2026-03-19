# 13. Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã. Faça um algoritmo que leia:• A distância da casa de Maria até sua irmã; O consumo do carro de Maria (KM rodados / litro); O preço da gasolina (litro). E mostre as informações que Maria necessita.

# Entrada

distancia = float(input("Qual a Distancia: "))
consumo = float(input("Quantos km por litro seu carro faz: "))
preço = float(input("Qual o Preço da gasolina: "))

# Processamento

quantidade = (distancia/consumo)
valor = (preço*quantidade)

# Saída
print (f"Precisará de {quantidade} litros de gasolina e gastará R${valor} para ir até sua irmã")

