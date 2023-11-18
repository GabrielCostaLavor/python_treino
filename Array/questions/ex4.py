nota = []

for i in range(4):
    number = int(input("Informer uma nota: "))
    nota.append(number)

for i in nota:
    print(i)

notaFinal = sum(nota) / len(nota)

print("Nota final: ",notaFinal)