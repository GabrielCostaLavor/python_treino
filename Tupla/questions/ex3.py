n = (10, 5, 8, 4)
m = (9, 2, 7, 8)
tupla = n + m
listTupla = list(tupla)
listTupla.sort()
lastList = []
for i in range(len(listTupla)):
    lastList.insert(0, listTupla[i])

tupla = tuple(lastList) 
print(tupla, lastList)