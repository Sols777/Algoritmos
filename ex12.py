# print("\nMenu - introduza um num")
# print('1 - para insderir 3 notas')
# print('2 - media dos 3 notas')
# print('3 - sooma das 3 notas')
# print('4 - Sair')

# nota1 , nota2 , nota3 = None , None , None

# op1 = int(input('opcao? - '))
# if op1 == 1:
#     nota1 , nota2 , nota3 = int(input("Nota 1- ")) , int(input("Nota 2- ")) , int(input("Nota 3- "))
#     print("\nMenu - introduza um num")
#     print('2 - media dos 3 notas')
#     print('3 - sooma das 3 notas')
#     print('4 - Sair')
#     op2 = int(input('opcao? - '))
#     match op2:
#         case 2:
#             media = (nota1 + nota2 + nota3) / 3
#             print ( f"A media dos 3 nums e {media}")
#         case 3:
#             soma = nota1 + nota2 + nota3
#             print ( f"A soma dos 3 nums e {soma}")
#         case 4:
#             print( "Byeeee")
#         case _:
#             print("Erro!!")
# else: 
#     print('Erro !!!!Escolha op 1!!!!!')
    
    
    
nota1, nota2, nota3 = None, None, None
 
print("\nMenu\n")
print("Prima 1 para ler a nota de 3 alunos (0 a 20)")
if nota1 and nota2 and nota3:
    print("Prima 2 para devolver a média de 3 alunos")
    print("Prima 3 para devolver a soma das notas de 3 alunos")
print("Prima 4 para sair")
op = int(input("Indique a sua opção: "))
 
 
match op:
    case 1:
        nota1, nota2, nota3 = int(input("Indique 3 notas: ")), int(input()), int(input())
    case 2:
        if nota1 and nota2 and nota3:
            print(f"Média: {(nota1+nota2+nota3)/3}")
        else:
            print("\nPor favor introduza as notas!")
    case 3:
        if nota1 and nota2 and nota3:
            print(f"Soma: {nota1+nota2+nota3}")
        else:
            print("\nPor favor introduza as notas!")            
    case 4:
        print("Hasta la vista")
    case _: #default
        print("\nErro: opção inválida")                                