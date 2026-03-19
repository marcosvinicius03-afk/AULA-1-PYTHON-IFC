#5. Faça um algoritmo que leia as 3 notas de um aluno e calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.

# Entrada
N1 = int(input("Primeira nota: "))
N2 = int(input("Segunda nota: "))
N3 = int(input("Terceira nota: "))

# Processamento
Média = (((N1 * 2) + (N2 * 3) + (N3 * 5)) /10)

# Saída
print ("essa é sua média: ", Média)