# valores 

TX_SS = 0.11
TX_IRS = 0.18

# LER
nome = input("Qual e o seu nome? ")
sal_bruto = float(input("Qual e o seu salario bruto? "))

# OPERACOES
sal_liquido = sal_bruto - sal_bruto*TX_SS - sal_bruto*TX_IRS

# ESCREVER

print(f'A pessoa com o nome: {nome} ira receber como salario liquido {sal_liquido :.2f} euros.')
