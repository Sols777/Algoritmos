valorIni = int(input(f'insira um valor inteiro\n -'))
cont  = 0
valor = valorIni
while True:
    if valor % 2 == 0:
        valor = valor/ 2
        cont += 1
    else:
        print (f'{valorIni} e divisivel por 2 , {cont} vezes')
        break
    