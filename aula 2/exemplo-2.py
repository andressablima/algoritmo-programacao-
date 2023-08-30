#Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas.
print('Digite as três notas: ')
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1+n2+n3)/3

print ('Média das notas é %.1f' %media) #%.1f significa que é valor float com uma casa decimal
