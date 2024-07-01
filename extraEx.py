# crie um programa que gere X (gerado entre 1 e 5) valores inteiros entre 1 e 30 e devolva a sua soma, média, max e min
from random import randint
 
num = randint(1, 5)
soma = 0
min = None
max = None
valoresGerados = ""
 
for i in range(num):
    val = randint(1, 30)
    valoresGerados += str(val) + " " # join
    soma += val
    if not min and not max:
        min = val
        max = val
    else:
        if val < min:
            min = val
        if val > max:
            max = val
 
print(f"""
      Número de elementos: {num}
      Listagem de elementos: {valoresGerados}
      Soma: {soma}
      Média: {soma/num :.2f}
      Max: {max}
      Min: {min}
      """)