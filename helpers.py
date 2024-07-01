#
def lerValorInteiro(msg='Erro',x=-2000,y=-2000):
    while True:
        try:
            val = int(input(msg))
        except:
            print("\nErro: deverá introduzir um valor inteiro\n")
        else:
            if x <= val <= y:
                return val
            print(f"\nErro: valor fora do intervalo[{x}:{y}]\n")
#            
def found(nums):
    temp = []
    for item in nums:
        if item not in temp:
            temp.append(item)
    return temp
#
def getQtValue(search, numbers):
    count = 0
    for num in numbers:
        if num == search:
            count += 1
    return count

def lerValorInteiroNaoNulos(msg='Erro'):
    while True:
        try:
            val = int(input(msg))
        except:
            print("\nErro: deverá introduzir um valor inteiro\n")
        else:
            return val
    
def lenghtList(lista):
    count = 0
    for item in lista:
        count += 1
    return count
# sum
def sumList(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma
def averageList(lista):
    soma = sumList(lista)
    count = lenghtList(lista)
    return soma / count

def elementExist(lista, valor):
    return valor in lista