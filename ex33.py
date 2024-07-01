#
from helpers import found, getQtValue, lerValorInteiro
#
numeros = [1,5,3,9,12,16,5,14,13,12]
# 
# def found(listaX , listaY):
#     temp = []
#     for item in listaX:
#         if item not in listaY:
#             temp.append(item)
#     for item in listaY:
#         if item in listaY:
#             listaY.remove(item)
#     return temp
#
# #
# def found(nums):
#     temp = []
#     for item in nums:
#         if item not in temp:
#             temp.append(item)
#     return temp

# def getQtValue(search, numbers):
#     count = 0
#     for num in numbers:
#         if num == search:
#             count += 1
#     return count
#

def printNonRepeatedValues(found, numbers):
    print("\nValores na lista e respetivas quantidades:\n")
    for num in sorted(found):
        print(f"{num} - {getQtValue(num, numbers)}")
#

printNonRepeatedValues(numeros , numeros)