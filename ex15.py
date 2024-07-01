somaTemp = 0

for i in range (6):
    temp = eval(input(f'Indique a temperatura do dia {i+1} (max 7 dias)'))
    somaTemp += temp
    
print(f'Media de temp da semana: {somaTemp/7 :.2f} graus celsius')
