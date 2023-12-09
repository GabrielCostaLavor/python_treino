totalNewContacts = int(input("Quantos contatos deseja adicionar: "))
contacts = {}

for i in range(totalNewContacts):
    name = input("Qual Nome do contato: ")
    contact = input("Qual Numero do contato: ")
    new = {
        "name": name,
        "contact": contact
    }
    contacts[name] = new

print(contacts)
search = input("Digite um nome parar buscar: ")

searchResult = contacts.get(search)

print(searchResult["contact"])