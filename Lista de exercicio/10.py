# 10. Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.

# Entrada
a = int(input("tempo de duração do evento em segundos: "))

# Processamento
b = int(a/3600)
c = int(a/60)

# Saída
print ("isso vale ",b, ("horas,"), c, ("minutos e "),a,("segundos"))