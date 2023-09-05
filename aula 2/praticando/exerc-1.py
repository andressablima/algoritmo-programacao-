# Escreva um programa em Python que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação. 

print('Digite dois números inteiros: ')
n1 = int(input())
n2 = int(input())

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
divi = n1/n2
divt = n1//n2
rest = n1 % n2
expo = n1 ** n2

print('O resultado da soma é: ', soma)
print('O resultado da subtração é: ', sub)
print('O resultado da multiplicação é: ', multi)
print('O resultado da divisão é: ', divi)
print('O resultado da divisão truncada é: ', divt)
print('O resultado do resto é: ', rest)
print('O resultado da exponenciação é: ', expo)
