# valores de 0 a 20 ate ser introduzido -1
numValid = 0

num = int(input(f'Introduza um valor entre 0 e 20: \n= '))

while True:
    if 0 < num > 20:
        print('num invalido')
    else:
        numValid += 1     
    num = int(input(f'{numValid + 1} - Introduza um valor entre 0 e 20: \n= '))
    if num == -1:
        print("Obrigada pela sua contribuicao!")
        break 
    
    
    
# count = 1
 
# while True:
#     val = int(input(f"{count} - Introduza um valor entre 0 e 20: "))
#     # condição de paragem
#     if val == -1:
#         print("Obrigado pela sua contribuição!")
#         break
#     # lógica
#     if 0 <= val <= 20:
#         count += 1
#     else:
#         print("\nValor inválido! Por favor insira novamente!\n")