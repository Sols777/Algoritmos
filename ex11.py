# question = 0
# soma = 0

# while question <= 4:
#     num = int(input('enter 5 values - '))
#     soma += num
#     print(f'Soma: {soma}')
#     question += 1

# print(f'Soma final e: {soma}')

soma = 0
contador = 0
# 1
val = int(input("Valor: "))
soma += val
contador += 1
print(f"Soma de {contador} valor(es): {soma}")
if contador == 1:
    max = val
    min = val
    posMin = 1
    posMax = 1
else:
    if val>max:
        max = val
        posMax = 1
    if val<min:
        min = val
        posMin = 1
#2 
val = int(input("Valor: "))
soma += val
contador += 1
print(f"Soma de {contador} valor(es): {soma}")
if contador == 1:
    max = val
    min = val
    posMin = 2
    posMax = 2
else:
    if val>max:
        max = val
        posMax = 2
    if val<min:
        min = val
        posMin = 2
#3
val = int(input("Valor: "))
soma += val
contador += 1
print(f"Soma de {contador} valor(es): {soma}")
if contador == 1:
    max = val
    min = val
    posMin = 3
    posMax = 3
else:
    if val>max:
        max = val
        posMax = 3
    if val<min:
        min = val
        posMin = 3
#4
val = int(input("Valor: "))
soma += val
contador += 1
print(f"Soma de {contador} valor(es): {soma}")
if contador == 1:
    max = val
    min = val
    posMin = 4
    posMax = 4
else:
    if val>max:
        max = val
        posMax = 4
    if val<min:
        min = val
        posMin = 4
#5
val = int(input("Valor: "))
soma += val
contador += 1
print(f"Soma de {contador} valor(es): {soma}")
if contador == 1:
    max = val
    min = val
    posMin = 5
    posMax = 5
else:
    if val>max:
        max = val
        posMax = 5
    if val<min:
        min = val
        posMin = 5


print(f'max = {max} na posicao {posMax} , min = {min} na posicao {posMin}')
