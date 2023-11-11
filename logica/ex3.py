totalView = int(input("Total de espectadores: "))
avarageAgeTypeThrid = 0
selectTypeThrid = 0
qtyPersonTypeOne = 0
avaragePersonTypeTwo = 0

for i in range(totalView):
    age = int(input('Qual a sua idade: '))
    opinion = int(input('Qual sua opnião sobre o filme: \n1-Regular; \n2-Bom, ; \n3-Excelente; '))
       
    if opinion == 1:
        qtyPersonTypeOne += 1
        
    if opinion == 2:
        avaragePersonTypeTwo += 1
        
    if opinion == 3:
        avarageAgeTypeThrid += age
        selectTypeThrid += 1
    
    
avarageAgeTypeThrid = avarageAgeTypeThrid/selectTypeThrid
avaragePersonTypeTwo = avaragePersonTypeTwo/totalView
print("Media das idades de quem respondeu excelente: ", avarageAgeTypeThrid)
print("Quantidade de pessoas que responderam regular: ", qtyPersonTypeOne)
print("Media das pessoas que responderam bom entre todos ", avaragePersonTypeTwo)