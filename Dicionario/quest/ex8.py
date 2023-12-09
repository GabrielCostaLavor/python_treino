products = {"tomate": [1000, 2.30],
 			"alface": [500, 0.45],
 			"batata": [2001, 1.20],
            "feijão": [100, 1.50]}

for i in range(1):
    product = input("Qual o produto que deseja comprar? ")
    productSelect = products.get(product)
    if productSelect: 
        print(productSelect)
        qty = int(input("Quantidade que deseja comprar? "))
        if productSelect[0] > qty:
            descount = productSelect[0] - qty
            products.get(product)[0] = descount
            
            print(products)
        else: print("Quantidade superior a do estoque")

    else: print("Produto não encontrado")
