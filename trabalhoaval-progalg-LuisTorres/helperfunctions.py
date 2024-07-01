# # Imports
from random import randint
# # Functions

# le apenas valores inteiros entre um intervalo especifico e manda
# msg de erro se invalido//
def lerValorInteiro(msg='Erro',x=1,y=50):
    while True:
        try:
            val = int(input(msg))
        except:
            print("\nErro: deverá introduzir um valor inteiro\n")
        else:
            if x <= val <= y:
                return val
            print(f"\nErro: valor fora do intervalo[{x}:{y}]\n")

# Gera nums 1 a 50 in inteiros que nao se repetem //
def getNums():
    lista = []
    for item in range(5):
        if item not in lista:
            lista.append(randint(1,51))
    return lista
# Gera estrelas 1 a 12 in inteiros que nao se repetem //
def getStars():
    lista = []
    for item in range(2):
        if item not in lista:
            lista.append(randint(1,13))
    return lista
# visual q que ta gerar nums //
def pinta(a , b):
    print(f'{b * a}')
# comparar as chaves
def found(listaX , listaY):
    temp = []
    for item in listaX:
        if item in listaY:
            temp.append(item)
    return sorted(temp) 
# quantos nums acertou
def lenghtList(lista):
    count = 0
    for item in lista:
        count += 1
    return count
# compara a chave com os possiveis primeiro e da return doo premio que ganhou
def winOrLose(val1,val2):
    chave=[]
    chave.append(val1)
    chave.append(val2)
    match chave:
        case [5 , 2]: 
            print('GANHOU!!!!!!! PRIMEIRO PREMIO!!!!!!!!!!!')
        case [5,1]:
            print('GANHOU!!!!!!! SEGUNDO PREMIO!!!!!!!!!!!')
        case [5,0]:
            print('GANHOU!!!!!!! TERCEIRO PREMIO!!!!!!!!!!!')
        case [4,2]:
            print('GANHOU!QUARTO PREMIO!')
        case [4,1]:
            print('GANHOU!QUINTO PREMIO!')
        case [3,2]:
            print('Ganhou!Sexto premio!')
        case [4,0]:
            print('Ganhou!Setimo premio!')
        case [2,2]:
            print('Ganhou!Oitavo premio!')
        case [3,1]:
            print('Ganhou!Nono premio!')
        case [3,0]:
            print('Ganhou!Decimo premio!')
        case [1,2]:
            print('Ganhou.Decimo primeiro premio!')
        case [2,1]:
            print('Ganhou.Penultimo premio!')
        case [2,0]:
            print('Ganhou.Ultimo premio!')
        case _:
            print('Ainda nao tens chave ou nao tens premio , va jogar de novo!')
            
            
# print do elementos com a formatacao certa
def printNums(list):
    # imprimir elementos ordenados separados por ,
    for i in range(len(list)):
        if i < len(list)-1: # último índice da lista
            print(list[i], end=' ')
        else:
            print(list[i] , end=' + ')
def printStars(list):
    # imprimir elementos ordenados separados por ,
    for i in range(len(list)):
        if i < len(list)-1: # último índice da lista
            print(list[i], end=' ')
        else:
            print(list[i])   