# funcoes

# so ints
def lerValorInteiro(msg,x,y):
    while True:
        try:
            val = int(input(msg))
        except:
            print("\nErro: deverá introduzir um valor inteiro\n")
        else:
            if x <= val <= y:
                return val
            print(f"\nErro: valor fora do intervalo[{x}:{y}]\n")
# n+n   
def soma(x,y):
    return x + y  
# n+a
def somaPlus(x,y,a):
    numX = x + a
    numY = y + a
    return numX , numY
# primeiros 10 numero impares
def dezImpar(num , max):
    if num % 2 == 0:
        num -= 1
    for i in range(num+2 , num+(max*2+1) , 2):
        print(i)
        


#######################################
# Valor int
num1 , num2 = lerValorInteiro('Valor1: ',0,20) , lerValorInteiro('Valor2: ',1,50)
print(f'valor 1 - {num1} , valor 2 - {num2}')
# soma
print(soma(num1,num2))
# soma 5
print (somaPlus(num1 , num2 , 5))
# primeiros 10
dezImpar(num1, 10)


