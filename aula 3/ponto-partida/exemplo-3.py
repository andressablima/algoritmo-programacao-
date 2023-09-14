#Ler dois números distintos e apresentar o quadrado do maior

import math

print("Digite 2 números: ")
n1 = float(input())
n2 = float(input())

if n1>n2:
    quadrado = math.pow(n1,2)
else:
    quadrado = math.pow(n2,2)
print('Quadrado do maior: ', quadrado)