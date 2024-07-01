#
seg,ter,qua,qui,sex,sab,dom = eval(input("Insira a temperatura dos dias desta semana: - ")) , eval(input('- ')),eval(input('- ')),eval(input('- ')),eval(input('- ')),eval(input('- ')),eval(input('- '))

# media 

tempMedia = (seg+ter+qua+qui+sex+sab+dom) / 7

print(f'A media de temperaturas esta semana e: {tempMedia :.1f} graus celsius.')