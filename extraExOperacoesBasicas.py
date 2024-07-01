# def

def found(listaX , listaY):
    temp = []
    for item in listaX:
        if item in listaY:
            temp.append(item)
    return sorted(temp) 
#

def check(lista):
    if lista:
        for item in lista:
            try:
                if isinstance(item, int):
                    return True
            except:
                print("\nErro: deverá introduzir um valor inteiro\n")
            else:
                return False
    return False
#  refactor
# def listExistInt(lista):
#     # criar uma função que verifique se a lista tem valores e estes são todos inteiros
#     if lista:
#         for item in lista:
#             if not isinstance(item, int):
#                 return False
#         return True
#     return False
 


# var
lista1 = [2,1,9,16,2,6,4,8,11]
lista2 = [1,3,4,31,12,45,11,2,12]

#

print(found(lista1 , lista2))

print(check(lista1))
print(check(lista2))