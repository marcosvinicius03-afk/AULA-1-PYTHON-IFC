# 6. Faça um algoritmo que leia as coordenadas de dois pontos, P1 (x1, y1) e P2 (x2, y2) respectivamente, e calcule e escreva a distância entre eles.

import math

# Entrada
x1 = float(input("valor de x1: "))
x2 = float(input("valor de x2: "))
y1 = float(input("valor de y1: "))
y2 = float(input("valor de y2: "))


# Processamento
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Saída
print ("A distancia entre os pontos é = ", distancia)