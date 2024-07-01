#
paisA = 80000
paisB = 200000
#
TXA = 0.03
TXB = 0.015
#
anos = 0

while True:
    if paisA > paisB:
        print(f'Passaram {anos} anos ate que o pais A ultrapassou o pais B em populacao')
        break
    paisA += paisA * TXA
    paisB += paisB * TXB
    anos += 1
