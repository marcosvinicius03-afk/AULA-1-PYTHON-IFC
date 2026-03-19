# 5. Elaborar um algoritmo para ler dois números e mostrar o quociente e o resto da divisão inteira do primeiro pelo segundo número.

# Entrada
n1 = float(input("Quanto vale o primeiro numero: "))
n2 = float(input("Quanto vale o segundo numero: "))

# Processamento
quociente = (n1//n2)
inteira = (n1%n2)

# Saida
print(f"O quociente vale {quociente:.2f} e o resto {inteira:.2f}")