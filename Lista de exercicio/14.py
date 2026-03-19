# 14. Faça um algoritmo que leia as medidas dos 4 lados de um terreno, o preço de um mourão e o preço de um metro de arame farpado. Deve ser escrito: o número de mourões necessários para cercar o terreno, colocando um mourão a cada 3 metros; o gasto total, o gasto em mourões e o gasto em arame, supondo que a cerca seja feita com 4 fios de arame.

# Entrada
t1 = float(input("Quanto vale o lado "))
t2 = float(input("Quanto vale o lado "))
t3 = float(input("Quanto vale o lado "))
t4 = float(input("Quanto vale o lado "))
mourao = float(input("Valor do mourão: "))
arame = float(input("Valor do metro de arame: "))

# Processamento
perimetro = (t1+t2+t3+t4)
quantidade = ((perimetro/3)+1)
gasto = ((quantidade*mourao)+ ((4*quantidade)*arame))

# Saída
print (f"Serão necessarios {quantidade} mouroes para cercar o terreno, o gasto total dos mouroes e Arames será de R${gasto} no total")