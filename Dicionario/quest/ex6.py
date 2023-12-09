personAll = []

for i in range(3):
    age = int(input("Qual sua idade: "))
    contact = input("Qual Numero do contato: ")
    personAll.append({
        "age": age,
        "contact": contact
    })

print(personAll)
print(personAll[0])