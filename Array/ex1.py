list = [False, "Gabriel", 10]

print(list)

listTwo = [10, 20, 30, 40]

print(listTwo)

listTwo.append(60)

print(listTwo)

#apagar
listTwo.remove(30)
del listTwo[0]

print(listTwo)

#Retornar o indece e o elemento 
listThrid = ['Gabriel', "Costa", "Lavor", "Morango"]

for i, element in enumerate(listThrid):
    print(i+1,"=> ",element)