
# nome = input('Como te chamas? ') # input devolve string
# idade = input('Idade: ') # input devolve string
# print(type(nome))
# print(type(idade))

# #  OPERADORES ARITMETICOS
# # >>> 2+2
# # 2
# # >>> 2-2
# # 0
# # >>> 2*2
# # 4
# # >>> 3*2
# # 6
# # >>> 3**2
# # 9
# # >>> 4/2
# # 2.0
# # >>> 4%2
# # 0
# # >>> 4//2
# # 2

# # IF 
# nota = 8
 
# if nota == 20:
#     print("Perfeito")
# elif nota >= 10:
#     print("Positiva")
# else:
#     print("Negativa")
    
# nota = 2
 
# if nota: # se nota existir
#     print(nota)

# nota = 11
# if nota % 2 == 0:
#     print(f"{nota} é par")
# else:
#     print(f"{nota} é impar")
    
    
# a = 3 
# b = 4

# a , b = b , a


##############################
# case == match

# print("\nMenu")
# print('1')
# print('2')
# print('3')
# print('4')
# print('5')

# op = int(input('opcao? - '))
# match op:
#     case 1 | 2:
#         print ( "1 ou 2")
#     case 3:
#         print ( "3")
#     case 4:
#         print ( "4")
#     case 5:
#         print ( "5")
#     case _:
#         print("Erro!!")

#########################
# FOR 
# for in range

# for i in range(10): # default incrementa 1 em 1 de 0 a 9
#     print(i)
    
# for i in range(1,11,2): # incrementa 2 em 2 ,= 1 , 3 , 5 , 7 , 9
#     print(i , end=' ')
        
##############################
# WHILE       
# num = 1
# while num<5:
#     print(f"Num: {num}")
#     num += 1

# ####################################
# #  DO WHILE / REPEAT 

# while True: # while 1
#     # instrucao
#     num = int(input('Valor: '))
#     # condicao de saida
#     if num == 0:
#         print("Terminou")
#         break # sai do ciclo mais proximo


# ###############################
# tratamento de erro para verificar se o input e inteiro
# while True:
#     try: # tentar executar
#         tabuada = int(input("Introduza um valor entre 1 e 10: "))
#     except: # tratamento de erro
#         print("\nErro: por favor introduza um número inteiro entre 1 e 10\n")
#     else: # se não der erro
#         if 1 <= tabuada <= 10:
#             break
#         print("\nErro: valor inválido\n")
 
# for i in range(1, 11):
#     print(f"{tabuada} * {i} = {tabuada*i}")

#########################
# # # FUNCOES 
# # declarar a função
# def maximo(a, b): # imprime uma mensagem
#     if a > b:
#         print(a)
#     else:
#         print(b)
 
# def maximov2(a, b): # retornar um valor
#     if a > b:
#         return a # devolve o valor de a
#     return b
 
# def ePar(val):
#     return val%2 == 0 # retornar o valor lógico de um condição
 
# def lerValores():
#     nome = input("Nome: ")
#     localidade = input("Localidade: ")
#     return nome, localidade
 
# # chamar a função
# """
# maximo(3, 2)
 
# print(maximov2(3, 2))
# max = maximov2(3, 2)
# if maximov2(3, 2) > 10:
#     pass
# """
# if ePar(int(input("Valor: "))):
#     print("Par")
 
# if not ePar(int(input("Valor: "))):
#     print("Impar")
 
# nome, localidade = lerValores()
#########################
# Still functions
# imports
 
# definição de funções
# def ePar(val):
#     return val%2 == 0 # retornar o valor lógico de um condição
 
# def lerValorInteiro():
#     while True:
#         try:
#             val = int(input("Val: "))
#         except:
#             print("\nErro: deverá introduzir um valor inteiro\n")
#         else:
#             return val
       
# def acrecentar(copia): # cópia
#     copia += 2
#     return copia
 
# # globals
# idade = lerValorInteiro() # 10
 
# # chamadas de funções
# idade = acrecentar(idade)
# print(idade)
 
 
 ##############################
 # Estruturas de dados
 # Listas
 
lista = [] # declarar uma lista vazia
# índices começam em 0 até n-1 (n número de elementos da lista)
#         0   1      2     3        4
#                                0 1 2
# lista2 = [1, 2.3, "sfdg", True, [1,2,3]] # nested list
 
# print(lista2[0])
# print(lista2[-1])


# for item in lista2:
#     #              var  type: float, int, str, list, dict, tuple # funciona em com qq tipo de dado
#     if isinstance(item, list): # verificar o tipo da variável
#         print("lista")
#     else:
#         print(type(item))
        
        
# lista.append('coisa boa')
# lista2 += ['sera que da?', 345 , True]

# # slices
# #del lista2[0]
# #print(lista2)
 
# # slices
# print(lista2[3:])
 
# lista3 = lista2[3:5]
 
# lista2[4] = "cocorococo"
# print(lista2)
# print(lista3)

# lista3 = list(range(1, 101))
# print(lista3)
# lista3 = [3,1,9,16,2,6,4,8]
# print(sorted(lista3)) # ordena MAS não altera a lista original
# lista3.sort() # ordena MAS altera a lista original
# print(lista3)
 
# for item in sorted(lista3):
#     print(item)
# lista = [3,1,9,16,2,6,4,8]
 
# lista2 = lista.copy()
 
# lista2[1] = 11
 
# print(lista)
# print(lista2)
## found something in something
# texto = "Olá eu QUERO pipocas! com muito caramelo"
# if "quero" in texto.lower():
#     print("Found it")