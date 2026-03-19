# 7. Faça um algoritmo que leia os valores a, b, c, d, e, f, e calcule x e y.

# Entrada
a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
e = float(input("valor de e: "))
f = float(input("valor de f: "))

# Processamento
x = (c * e- b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

# Saída
print ("Os pontos x e y são, respectivamente: ", x, y)
