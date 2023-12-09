car = [{
    "Marca": "Fiat",
    "Modelo": "Argo",
    "Ano": 2020,
    "Options": ["pneus", "ar", "vidro"]
}, {
    "Marca": "Renault",
    "Modelo": "Sandero",
    "Ano": 2016,
    "Options": ["pneus", "ar", "tapete"]
}]


print(car[0]["Options"][1])

carTwo = {
    "Marca": "Fiat",
    "Modelo": "Argo",
    "Ano": 2020,
    "Options": ["pneus", "ar", "vidro"]
}

carTwo.update({"cor": "Azul"})

print(carTwo)
print(carTwo.keys())
print(type(carTwo.values()))