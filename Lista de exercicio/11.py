# 11. O governador acaba de liberar R$ 1.000.000.000,00 para construção de casas populares. Cada casa custa o equivalente a 90 salários mínimos. Faça um algoritmo que leia o valor do salário mínimo e calcule a quantidade de casas que podem ser construídas com o recurso liberado.

# Entrada
minimo = int(input("Qual o valor do salario minimo R$ "))

# Processamento
casa = int (minimo * 90)
Quantidade = int(1000000000/casa)

# Saida
print(f"com o salario minimo de R${minimo}, será possivel construir {Quantidade} casas")