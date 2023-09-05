import math
print("Digite o valor do custo e o valor do ingresso: ")

custo = float(input())
ingresso = float(input())

custo_alcancado = math.ceil(custo/ingresso)

qt_lucro = math.ceil((custo+custo*0.23)/ingresso)

print(custo_alcancado, qt_lucro)