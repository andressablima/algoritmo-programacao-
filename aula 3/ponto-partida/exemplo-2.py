# Condicional Composta
# Programa que leia número inteiro e exiba se ele é um número par ou ímpar

n1 = float(input("Digite um número: "))
if n1%2==0: #Resto por 2
    print('%.1f é par.' %n1) #mostrar numero float com uma casa decimal.
else:
    print('%.1f é ímpar' %n1)