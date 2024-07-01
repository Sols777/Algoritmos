# IMPORTS
from helperfunctions import *
# Euromilhoes

# validacao
# 5 numeros de 1 a 50
# 2 estrelas de 1 a 12
# valores nao repetidos , temq que ser inteiros maiores que 0

# num do jogador/ estrelas do jogador + nums do sorteio/estrelas do sorteio

# sorted 1 23 31 46 12 + 5 8

# atribui premio de depende
############################################################
#variaveis globais
playerReady = False
numsPlayer = []
starsPlayer = []
numsSorteio= []
starsSorteio = []
foundNums = []
foundStars = []
#   
   
########## MENU ###########
print(f'**********************')
print(f'Jogo do Euromilhoes')
print(f'**********************')
while True:
    print(f'\n1 - Para Jogar')
    print(f'\n2 - Sorteio')
    print(f'\n3 - Premios')
    print(f'\n4 - Sair')
    op = int(input(f'Escolhe uma opcao: '))
    match op:
        case 1: # jogar
            print(f'*****Menu Jogar**************')
            print(f'\n1 - Inserir chave manualmente')
            print(f'\n2 - Gerar chave automaticamente')
            jogo = int(input('Opcao: '))
            if jogo == 1:
                numsPlayer = []
                starsPlayer = []
                print('Insira os nums(1 a 50): ')
                for item in range(5):
                    nums = lerValorInteiro (f'{item+1} numero: ',1 , 50)
                    numsPlayer.append(nums)
                print('Insira as estrelas(1 a 12): ')
                for item in range(2):
                    stars = lerValorInteiro (f'{item+1} numero: ',1 , 12)
                    starsPlayer.append(stars)
                print(f'\nEscolheu a chave:')
                printNums(sorted(numsPlayer)) , printStars(sorted(starsPlayer))
            elif jogo == 2:
                numsPlayer = getNums()
                starsPlayer = getStars()
                print('\nCHAVE DA SORTE GERADA:')
                printNums(numsPlayer) , printStars(starsPlayer)
            elif jogo != 1 and jogo != 2:
                print('Introduza um valor valido por favor')
            playerReady = True
        case 2: # sorteio\
            if playerReady: # sorteio apenas comeca quando o player inserir uma chave
                numsSorteio= getNums()
                starsSorteio = getStars()
                print('A gerar chave da sorte......')
                for i in range (1, 5):
                    pinta(i,'*')
                ###########################
                print('\nCHAVE DA SORTE')
                printNums(sorted(numsSorteio)) , printStars(sorted(starsSorteio))
                print('ORDEM DE SAIDA:')
                printNums(numsSorteio) , printStars(starsSorteio)
                # print(f'Chave: {sorted(numsSorteio)} + {sorted(starsSorteio)} | Ordem de saida: {numsSorteio} + {starsSorteio}')
                print('######################')
                print(f'Chave do jogador:')
                printNums(sorted(numsPlayer)) , printStars(sorted(starsPlayer))
                foundNums = found(numsSorteio,numsPlayer)
                foundStars = found(starsSorteio,starsPlayer)
                print(f'Acertas te em {lenghtList(foundNums)} numeros e em {lenghtList(foundStars)} estrelas')
                if lenghtList(foundNums) <= 1:
                    print(f'\nAVISO:Nao ganhas te nada!Podes premir sorteio para gerar um sorteio novo (nova chave da sorte)!')
                else:
                    print(f'\nAviso:Parece que ganhaste alguma coisa , vai a premios para descobrir!!!!')
            else:
                print('AVISO:O jogador ainda nao escolheu uma chave da sorte....')
        case 3: # premios
            print('''
                     Premios possiveis      | ACERTOS
                  1.Premio                  | 5 Numeros + 2 estrelas
                  2.Premio                  | 5 Numeros + 1 estrelas
                  3.Premio                  | 5 Numeros + 0 estrelas
                  4.Premio                  | 4 Numeros + 2 estrelas
                  5.Premio                  | 4 Numeros + 1 estrelas
                  6.Premio                  | 3 Numeros + 2 estrelas
                  7.Premio                  | 4 Numeros + 0 estrelas
                  8.Premio                  | 2 Numeros + 2 estrelas
                  9.Premio                  | 3 Numeros + 1 estrelas
                  10.Premio                 | 3 Numeros + 0 estrelas
                  11.Premio                 | 1 Numeros + 2 estrelas
                  12.Premio                 | 2 Numeros + 1 estrelas
                  13.Premio                 | 2 Numeros + 0 estrelas
                  ''')
            nums = int(lenghtList(foundNums))
            stars = int(lenghtList(foundStars))
            winOrLose(nums,stars)
            # else:
            #     print('Sem premio ou sem chave , va jogar de novo porfavor!')
        case 4: # sair
            print('Adeuuus ............')
            break
       