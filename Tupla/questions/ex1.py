list = []
for i in range(5):
    number = int(input("Adicione um valor para tupla: "))
    if number % 2 != 0:
        list.append(number)

tupla = tuple(list)

print(tupla)