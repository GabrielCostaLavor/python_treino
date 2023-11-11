allTeam = ['Brasil', 'Espanha']
bigSize= 0
allSizeAverage = 0
allAgeAverage = 0
totalPlayers = 2

print(len(allTeam))
for team in allTeam:
    sizeAverage = 0
    ageAverage = 0
    bigSizeTeam = 0
    newestTeam = 0
    
    for i in range(totalPlayers):
        size = int(input("Qual seu peso: "))
        age = int(input("Qual sua idade: "))
        
        if size>bigSize: 
            bigSize = size
            
        if size>bigSizeTeam:
            bigSizeTeam = size
            
        if newestTeam>=age or newestTeam == 0: 
            newestTeam = age
            
        sizeAverage += size/totalPlayers
        ageAverage += age/totalPlayers
        allSizeAverage += size/(totalPlayers * len(allTeam))
        allAgeAverage += age/(totalPlayers * len(allTeam))
    print(f"Peso medio dos jogadores de {team}: ", sizeAverage)
    print(f"Idade media dos jogadores de {team}: ", ageAverage)
    print(f"Atleta mais pesado do/a {team}: ", bigSizeTeam)
    print(f"Atleta mais jovem do/a {team}: ", newestTeam)
            
        
        
print(f"Peso medio de todos os jogadores: ", allSizeAverage)
print(f"Idade media de todos os jogadores: ", allAgeAverage)