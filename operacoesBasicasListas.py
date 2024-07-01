# max , min , sum , count , search , average

# len
def lenghtList(lista):
    count = 0
    for item in lista:
        count += 1
    return count
# max
def maxList(lista):
    max = lista[0]
    for item in lista:
        if item > max:
            max = item
    return max
# min
def minList(lista):
    min = lista[0]
    for item in lista:
        if item <= min:
            min = item
    return min
# sum
def sumList(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma
# count
def countList(lista , x):
    count = 0
    for item in lista:
        if x == item:
            count +=1
    return count
# search
def searchList(lista , x):
    for item in lista:
        if x == item:
            return True
    return False
# average
def averageList(lista):
    soma = sumList(lista)
    count = lenghtList(lista)
    return soma / count
# var

lista1 = [3,1,9,16,2,6,4,8,1]

#

print (lenghtList(lista1)) # done
print (maxList(lista1)) # done
print (minList(lista1)) # done
print (sumList(lista1)) # done
print (countList(lista1 , 1)) # done
print (searchList(lista1 , 16)) # done
print (averageList(lista1)) # done