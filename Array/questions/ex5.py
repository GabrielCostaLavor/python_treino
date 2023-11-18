list = []

for i in range(4):
    number = int(input("Informer sua idade: "))
    list.append(number)

print("Maior idade: ",max(list))
print("Menor idade: ", min(list))