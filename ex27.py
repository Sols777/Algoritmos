from helpers import lerValorInteiro
# funcoes 
def converterHora(hora , min):
    formato = 'AM'
    if hora > 12:
        hora -= 12
        formato = 'PM'
    print(f'{hora}:{min} {formato}')

# 
horas = lerValorInteiro('Introduza a hora atual:\n- ', 0 , 23)
mins = lerValorInteiro('Introduza o minuto atual:\n- ' , 0 , 59)

converterHora(horas, mins)