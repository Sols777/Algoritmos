# helper function
def elementExist(lista, valor):
    return valor in lista
 
def removeElement(lista, valor):
    count = 0
    for item in lista:
        if item == valor:
            lista.remove(valor)
            count += 1
    return count
 
def removeElementsFromList(lista, valor):
    temp = []
    count = 0
    for item in lista:
        if item != valor:
            temp.append(item)
        else:
            count += 1
    return temp, count
 
numeros = [1,5,3,9,12,16,5,14,13,12]
 
while True:
    op = input("Número a remover: ")
    # condição de paragem
    if op.lower() == "fim":
        break
    if numeros:
        if elementExist(numeros, int(op)):
            #print(f"Foram removidos {removeElement(numeros, int(op))} elementos!")
            numeros, count = removeElementsFromList(numeros, int(op))
            if count:
                print(f"Foram removidos {count} elementos!")
 
        else:
            print(f"\nO número {int(op)} não foi encontrado!\n")
    print("\nListagem de números: \n")
    print(numeros)
 