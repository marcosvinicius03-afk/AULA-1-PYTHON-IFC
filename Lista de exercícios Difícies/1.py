# 1. Fazer um algoritmo para ler o valor do lado de um quadrado e mostrar sua área ( lado2) e seu perímetro ( 4 x lado ).

# Entrada
lado = float(input("Quanto vale o lado: "))

# Processamento
area = (lado**2)
perimetro = (4*lado)

# Saida
print(f"A Área vale: {area:.2f}\nPerimetro vale: {perimetro:.2f}")