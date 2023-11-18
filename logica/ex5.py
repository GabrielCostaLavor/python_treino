totalClient = 3
totalBalance = 0
daily = 30

for i in range(1):
    client = []
    for i in range(totalClient):
        name = input("Qual nome do cliente: ")
        numberAccont = int(input("Qual o numero da conta: "))
        days = int(input("Total de dias de na pousada: "))
        value = 0

        if days <= 10: 
            value = (days * daily) + (days * 15)
        if days > 10:
            value = (days * daily) + (days * 8)

        totalBalance += value
        
        print(f"Nome do cliente: {name}")
        print(f"Numero da conta do cliente: {numberAccont}")
        print(f"Valor da conta do cliente: {value}")
    print(f"Total faturado pela pousada: {totalBalance}")    