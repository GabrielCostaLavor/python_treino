lista = [1,2,6,9,5,2]
setList = set(lista)
print("Set: ",setList)
print(setList.pop())

if 9 in setList:
    print("Numero 9 existe")
else:
    print("Numero 9 não existe")

setList.add(10)
print(setList)
setList.remove(5)
print(setList)
newSet = setList.copy()
print(newSet, setList)

newSetTwo = {29,30,1}
setList.update(newSetTwo)
print(setList)
lastSet = newSet.union(newSetTwo)
print(setList, lastSet)
