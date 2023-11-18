a = [10, 20, 30]
b = a
a.append(40)
#ambos vão fazer referencia a mesma lista
print(a, b)

c = a[:]
a.append(50)
print(a, c)

#Somar todos os valores
print(sum(a))
#Tamanho da lista
print(len(a))
#Valor maximo e minimo da lista
print(max(a))
print(min(a))