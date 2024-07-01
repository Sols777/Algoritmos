
def createNewPerson():
    print("\nRegisto de nova pessoa:\n")
    # bi, nome, idade, salário
    bi = int(input("BI: ")) # 0
    name = input("Nome: ") # 1
    age = int(input("Idade: ")) # 2
    wage = eval(input("Salário: ")) # 3
    return [bi, name, age, wage]
 
def printPersonData(person):
    print(f"""
          Nome: {person[1]} Idade: {person[2]}
          BI: {person[0]} Salário: {person[3] :.2f}€""")
   
def printAllPersons(listPersons):
    print("Listagem de pessoas:")
    if listPersons:
        for person in listPersons:
            printPersonData(person)
    else:
        print("\nAinda não foram adicionadas pessoas\n")
 
def getPersonsSalaryBiggerThenX(listPersons, salary):
    print(f"Listagem de pessoas cujo salário é maior que {salary}€:")
    if listPersons:
        for person in listPersons:
            if person[3] > salary:
                printPersonData(person)
    else:
        print("\nAinda não foram adicionadas pessoas\n")    
 
def getPersonsBetwwenAge(listPersons, minAge, maxAge):
    print(f"Listagem de pessoas cuja idade está no intervalo [{minAge}:{maxAge}]:")
    if listPersons:
        for person in listPersons:
            if minAge <= person[2] <= maxAge:
                printPersonData(person)
    else:
        print("\nAinda não foram adicionadas pessoas\n")        
 
def menu(listPersons):
    while True:
        op = input("Pretende inserir uma nova pessoa (s/n)? ")
        if op.lower() == 'n':
            #printAllPersons(listPersons)
            #getPersonsSalaryBiggerThenX(listPersons, float(input("Salário: ")))
            getPersonsBetwwenAge(listPersons, int(input("Idade mínima: ")), int(input("Idade máxima: ")))
            break
        elif op.lower() == 's':
            listPersons.append(createNewPerson())
        else:
            print("\nErro: opção inválida\n")
 
def addInitialValues():
    temp = []
    temp.append([123, "Carla", 23, 1229.23])
    temp.append([321, "Zé", 54, 2435])
    temp.append([111, "Sofia", 18, 950])
    temp.append([222, "Manel", 45, 6500])
    temp.append([333, "Rafael", 65, 1220])
    return temp
 
#listPersons = []
listPersons = addInitialValues()
menu(listPersons)
 