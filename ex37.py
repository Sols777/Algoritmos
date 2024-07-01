#
from helpers import *
#
lista1 = [3,9,12,4,2,8,5,1]
lista2 = list(range(1,21))

def compare(lista1, lista2):
    temp = []
    for item in lista1:
        if item in lista2:
            temp.append(item)
    return sorted(temp)



def printListContent(list):
    # imprimir elementos ordenados separados por ,
    for i in range(len(list)):
        if i < len(list)-1: # último índice da lista
            print(list[i], end=', ')
        else:
            print(list[i])
   
    for index, value in enumerate(list):
        if index < len(list)-1:
            print(value, end=', ')
        else:
            print(value)
    """
    for val in list:
        print(val, end=', ')
    """
#
lista = compare(lista1 , lista2)

#
print(f"""
      lista 1: {lista1}
      lista 2: {lista2}
      """)


printListContent(lista)