numberUserCosume = []
totalUserCosumeValue = []
totalTypeResidencial = 0
totalTypeComercial= 0
totalTypeIndustrial = 0
mediaConsumeOneAndTwo = 0

while True:
    numConsume = int(input('Informe o numero do consumidor:'))
    if numConsume != 0:
        qtyKwh = int(input('Informe a quantidade de KWH:'))
        consumeType = int(input('Informe o tipo do consumidor: \n1-residencial; \n2-comercial, ; \n3-industrial, ; '))
        consumeTotal = 0
        taxa= 0
        
        if consumeType == 1:
            consumeTotal = qtyKwh * 0.3
            mediaConsumeOneAndTwo += consumeTotal / 2
            totalTypeResidencial += consumeTotal
            
        elif consumeType == 2:
            consumeTotal = qtyKwh * 0.5
            mediaConsumeOneAndTwo += consumeTotal / 2
            totalTypeComercial += consumeTotal
            
        elif consumeType == 3:
            consumeTotal = qtyKwh * 0.7
            totalTypeIndustrial += consumeTotal
            
        format = f"Consumidor {numConsume}: {consumeTotal}"
        totalUserCosumeValue.append(format)
        print(consumeTotal)
    else: 
        print("Programa finalizado")
        totalALConsume = totalTypeIndustrial + totalTypeResidencial + totalTypeComercial
        for user in totalUserCosumeValue:
            print(user)
            
        print("Consumo total do industrial: ", totalTypeIndustrial )
        print("Consumo total do Residencial: ", totalTypeResidencial )
        print("Consumo total do Comercial: ", totalTypeComercial )
        
        print("Medial dos consumidores Residencial e comercial", mediaConsumeOneAndTwo )
        print("Consumo total de todos os consumidores", totalALConsume )
        
        
        break;
else: print("Programa finalizado")