# valores

DIA = 12 
MES = 7
ANO = 2022

# funcoes
def mesFull(mes):
    match mes:
        case 1:
           return "Janeiro"
        case 2:
           return "Fevereiro"
        case 3:
           return "Marco"
        case 4:
           return "Abril"
        case 5:
           return "Maio"
        case 6:
           return "Junho"
        case 7:
           return "Julho"
        case 8:
           return "Agosto"
        case 9:
           return "Setembro"
        case 10:
           return "Outobro"
        case 11:
           return "Novembro"
        case 12:
           return "Dezembro"

def data(dia , mes ,ano):
    print(f'dia {dia} do mes {mesFull(mes)} de {ano}')


data(DIA , MES , ANO)