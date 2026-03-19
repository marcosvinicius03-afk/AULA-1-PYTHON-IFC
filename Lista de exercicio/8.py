# 8. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

# Entrada
a = float(input("Custo de fábrica: "))

# Processamento
b = float(28/100 * a)
c = float(45/100 * a)
d = float(a + b + c)

# Saída
print ("O custo ao consumidor é: ", d)