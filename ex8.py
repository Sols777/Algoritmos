# 2 int em input  , devolve a some , e verifica dse sao par ou impar

#LER INPPUT
num1 , num2 = int(input('Insira dois numeros inteiros: - ')) , int(input('- '))

# OPERACOES
soma = num1 + num2
multi = num1 * num2
div1 = num1 / num2 
div2 = num2 / num1
sub1 = num1 - num2
sub2 = num2 - num1

# PAR OU IMPAR 
if num1 % 2 == 0:
    print(f'f{num1} e par')
else:
     print(f'{num1} e impar')

if num2 % 2 == 0:
    print(f'{num2} e par')
else:
     print(f'{num2} e impar')

# OUTPUT

print(f'0 resultado da soma dois numeros e: {soma} ')
print(f'0 resultado da multiplicacao dois numeros e: {multi} ')
print(f'0 resultado da divisao do primeiro num com o segundo e: {div1} ')
print(f'0 resultado da divisao do segundo num com o primeiro e: {div2} ')
print(f'0 resultado da subtracao do primeiro num menos o segundo e: {sub1} ')
print(f'0 resultado da subtracao do segundo num menos o primeiro e: {sub2} ')