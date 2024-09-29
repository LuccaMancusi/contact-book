class Contact:
    def __init__(self, name, phone, email, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite
    def mark_as_favorite(self):
        self.favorite = True
    def remove_favorite_mark(self):
        self.favorite = False
    def is_favorite(self):
        return self.favorite

def append_contact(contacts):
    name = input("Digite o nome do novo contato: ")
    phone = input("Digite o telefone do novo contato: ")
    email = input("Digite o email do novo contato: ")
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    print("\nContato adicionado com sucesso!")
    return

def show_contacts(contacts):
    print("\nLista de contatos: ")
    for index, contact in enumerate(contacts):
        msg = "[★]" if contact.favorite else "[ ]"
        print(f"\nId: {index + 1}")
        print(f"Nome: {contact.name}")
        print(f"Telefone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Favorito: {msg}")   
    return

def mark_favorite_contact(contacts):
    contact_index = int(input("\nDigite o id do contato que deseja marcar como favorito: "))
    if (contact_index < 1 or contact_index > len(contacts)):
        print("Este id não é válido! ")
        return
    else:
        contacts[contact_index - 1].mark_as_favorite()
        print(f"\nContato {contact_index} marcado como favorito!")
        return

def unmark_favorite_contact(contacts):
    contact_index = int(input("\nDigite o id do contato que deseja desmarcar como favorito: "))
    if (contact_index < 1 or contact_index > len(contacts)):
        print("Este id não é válido! ")
        return
    else:
        contacts[contact_index - 1].remove_favorite_mark()
        print(f"\nContato {contact_index} desmarmarcado como favorito!")
        return

def show_favorite_contacts(contacts):
    print("\nLista de contatos favoritos:")
    for index, contact in enumerate(contacts):
        if contact.is_favorite():
            msg = "[★]" if contact.favorite else "[ ]"
            print(f"\nId: {index + 1}")
            print(f"Nome: {contact.name}")
            print(f"Telefone: {contact.phone}")
            print(f"Email: {contact.email}")
            print(f"Favorito: {msg}")   
    return

def delete_contact(contacts):
    contact_index = int(input("\nDigite o ID do contato que deseja remover: "))
    if (contact_index < 1 or contact_index > len(contacts)):
        print("Este id não é válido!")
        return
    else:
        contacts.remove(contacts[contact_index - 1])
        print(f"\nContato {contact_index} removido com sucesso!")
        return