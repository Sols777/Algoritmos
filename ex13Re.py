
nota1, nota2, nota3 = None, None, None
 
while True:
    print("\nMenu\n")
    print("Prima 1 para ler a nota de 3 alunos (0 a 20)")
    if nota1 != None and nota2 != None and nota3 != None:
        print("Prima 2 para devolver a média de 3 alunos")
        print("Prima 3 para devolver a soma das notas de 3 alunos")
    print("Prima 4 para sair")
    op = int(input("\nIndique a sua opção: "))
 
    match op:
        case 1:
            while True:
                nota1 = int(input("Nota 1: "))
                if 0 <= nota1 <= 20:
                    break
                print("\nErro: olha aiiiiiiii: nota entre 0 e 20!\n")
            while True:
                nota2 = int(input("Nota 2: "))
                if 0 <= nota2 <= 20:
                    break
                print("\nErro: olha aiiiiiiii: nota entre 0 e 20!\n")
            while True:
                nota3 = int(input("Nota 3: "))
                if 0 <= nota3 <= 20:
                    break
                print("\nErro: olha aiiiiiiii: nota entre 0 e 20!\n")                                
        case 2:
            if nota1 != None and nota2 != None and nota3 != None:
                print(f"Média: {(nota1+nota2+nota3)/3}")
            else:
                print("\nPor favor introduza as notas!")
        case 3:
            if nota1 != None and nota2 != None and nota3 != None:
                print(f"Soma: {nota1+nota2+nota3}")
            else:
                print("\nPor favor introduza as notas!")            
        case 4:
            print("Hasta la vista")
            break
        case _: #default
            print("\nErro: opção inválida")                                