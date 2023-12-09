cars = {} 
modeloMaisEconomico = ""
valorMaisEconomico = 0

for i in range(3):
    modelo = input("Qual o nome do modelo do carro: ")
    kmPorLitro = int(input("Quantos KM por litro de combustível: "))
    totalGasto = int (1000 / kmPorLitro) * 5.25
    print(totalGasto)
    cars[modelo] = {
        "modelo": modelo,
        "km": kmPorLitro,
        "total": totalGasto
    }
    if totalGasto < valorMaisEconomico or valorMaisEconomico == 0:
        valorMaisEconomico = totalGasto
        modeloMaisEconomico = modelo

print(cars)
print(cars[modeloMaisEconomico])