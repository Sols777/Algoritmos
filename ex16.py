somaNotas = 0

##
numAlunos = int(input(f'Insira do num de alunos desta turma \n - '))

for i in range (1 , numAlunos+1):
    nota = eval(input(f'Insira a nota (0 a 20) do aluno {i}:\n - '))
    somaNotas += nota
    if  nota >= 10:
        print(f'O aluno {i} esta Aprovado')
    else:
        print(f'O aluno {i} esta Reprovado')
    if i == 1:
        max = nota
        min = nota
    else:
            if nota>max:
                max = nota
            if nota<min:
                min = nota


        
media = somaNotas / numAlunos

print(f'A media das notas e {media :.2f}')
print (f'Nota min {min} e nota max {max}')