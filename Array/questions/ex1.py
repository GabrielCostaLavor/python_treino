list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listPar = []
listImpar = []

print("Inicial: ",list)
list.reverse()
print("Lista decrecente: ", list)
list.sort()
print("Ordem crescente: ", list)
list.append(27)
print(list)
list.remove(9)
print(list)
list.pop(10)
print(list)
print("Soma de todos os valores: ", sum(list))
print("Menor elemento da lista: ", min(list))

for el in list:
    if el % 2 == 0:
        listPar.append(el)
    else:
        listImpar.append(el)
        
print("Lista de numeros pares ", listPar)
print("Lista de numeros impares: ", listImpar)
list.insert(4, 89)
list.insert(4, 91)
print("Lista final: ",list)
print(len(list))