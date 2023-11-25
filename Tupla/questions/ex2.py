prova1 = (10, 5, 8, 4)
prova2 = (9, 2, 7, 8)
provas = [prova1, prova2]
melhorNota = 0
melhorProva = 0

for i in range(len(provas)):
    print(provas[i])
    valueTotal= 0
    for indexTupla in range(len(provas[i])):
        valueTotal += provas[i][indexTupla]
        
    mediaProva = valueTotal / len(provas[i])
    if mediaProva > melhorNota:
        melhorNota = mediaProva
        melhorProva = i+1
    print(f"Media da prova {i+1}: {mediaProva}")

print(f"A melhor prova foi a {melhorProva} com a media de: ", melhorNota)