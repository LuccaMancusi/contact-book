class Contact:
    def __init__(self, name, phone, email, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite

def append_contact(contacts):
    name = input("Digite o nome do novo contato: ")
    phone = input("Digite o telefone do novo contato: ")
    email = input("Digite o email do novo contato: ")
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    print("\nContato adicionado com sucesso!")
    input("Digite qualquer coisa para voltar ao menu")
    return

def show_contacts():
    pass

def mark_favorite_contact():
    pass

def unmark_favorite_contact():
    pass

def show_favorite_contacts():
    pass

def delete_contact():
    pass