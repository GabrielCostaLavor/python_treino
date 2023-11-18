ageSmall = ageBig = 0

for i in range(30):
    age = int(input("Qual a sua idade: "))

    if age < 21:
        ageSmall += 1
    if age > 50: 
        ageBig += 1


print(f"Total de pessoas com menos de 21: {ageSmall}")
print(f"Total de pessoas com mais de 50: {ageBig}")
