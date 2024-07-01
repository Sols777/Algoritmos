while True:
    
    num = int(input(f'Insira um valor inteiro entre 1 e 10\n- '))
    if 0 < num <=10:
        break
    else:
        print ('erro , introduza de novo')
    
temp = num
for i in range (1,11,1):
    temp = num * i
    print (f'{num} * {i} = {temp}')
    i += num