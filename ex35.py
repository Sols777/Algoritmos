# imports
from helpers import lerValorInteiroNaoNulos , averageList , sumList , lenghtList
#
nums = []
while True:
    num = lerValorInteiroNaoNulos('Introduza nums inteiros positivos e nao nulos , insira 0 para terminar\n- ')
    if num > 0:
        nums.append(num)
    if num == 0:
        print('thank you')
        break
    else:
        print('erro!!')

len = lenghtList(nums)
sum = (sumList(nums))
print('\nMedia:\n')    
print((averageList(nums)))