# 15. São dados de entrada sobre um automóvel: modelo, marca, ano, km inicial, km final,litros de combustível consumidos, preço por litro. Faça um algoritmo que escreva os dados de saída da seguinte forma: modelo_______________________ marca______________ ano________ distância percorrida ________________ litros de combustível consumidos _____________ preço por litro R$ _____________ total a pagar R$ ______________ km por litro __________

from IPython.core.display import clear_output

# Entrada
modelo = input("Qual o modelo: ")
marca = input("Qual a marca: ")
ano = int(input("Qual o ano: "))
kmi = int(input("Km inicial: "))
kmf = int(input("Km final: "))
litro = int(input("Quanto custa o preço da gasolina: "))
consumo = int(input("Qual o Consumo de Combustivel por km: "))

# Processamento
kmp = (kmf - kmi)
combustivel = (kmp/consumo)
total = (combustivel*litro)

# Saida
clear_output()
print(f"\n\nModelo: {modelo} Marca: {marca} Ano: {ano}\n Distância percorrida: {kmp}\n Litros de combustível consumidos: {combustivel}\n preço por litro: {litro}\n Total a pagar: R${total}\n km por Litro: {consumo}")
