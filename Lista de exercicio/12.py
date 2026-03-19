# 12. Faça um algoritmo que leia o salário bruto mensal de um funcionário, calcule e mostre os valores conforme modelo abaixo: Salário Bruto:R (−)IR(15  (-) INSS (11%) :R (−)Sindicato(3  Salário Líquido :R$

# Entrada
salario = int(input("Quanto você ganha: R$"))

# Processamento
ir = (salario*0.15)
inss = (salario*0.11)
sindicato = (salario*0.03)
liquido = (salario - (ir+inss+sindicato))

# Saída
print (f"IR = R${ir}")
print (f"INSS = R${inss}")
print (f"Sindicato = R${sindicato}")

print (f"Com os descontos você ganha: R${liquido}")