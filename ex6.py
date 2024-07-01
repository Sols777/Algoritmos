

nome = input('Indique o seu nome: ')
diasTrab = eval(input('Quantos dias trabalhou este mes? '))
subDia = eval(input('Qual o valor do subsidio diario? '))

subMensal = subDia * diasTrab

print(f'O(a) {nome} tem direito a {subMensal :.2f} euros de Subsidio.')