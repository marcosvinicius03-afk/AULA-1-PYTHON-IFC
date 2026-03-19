# 3. Fazer um algoritmo para ler os valores da base e altura de um retângulo e mostrar seu perímetro ( 2 x ( base + altura ) ) e sua área ( base x altura ).

# Entrada
altura = float(input("Quanto vale a altura: "))
base = float(input("Quanto vale a base: "))

# Processamento
perimetro = (2*(base+altura))
area = (base*altura)

# Saida
print(f"O perimetro vale {perimetro:.1f} e a área {area:.1f}")