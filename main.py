from contacts import append_contact, show_contacts, mark_favorite_contact, unmark_favorite_contact, show_favorite_contacts, delete_contact

def show_menu():
    print("\n------------------------------------")
    print("Agenda de contatos: ")
    print("1. Adicionar contato")
    print("2. Visualizar contatos cadastrados")
    print("3. Marcar contato como favorito")
    print("4. Desmarcar contato como favorito")
    print("5. Ver lista de contatoas favoritos")
    print("6. Apagar contato")
    print("7. Sair do programa")

def break_action():
    input("\nDigite qualquer coisa para voltar ao menu")

contacts = []

while True:
    show_menu()
    try:
        option = int(input("Digite uma opção: "))
        if option == 1:
            append_contact(contacts)
            break_action()
        elif option == 2:
            show_contacts(contacts)
            break_action()
        elif option == 3:
            show_contacts(contacts)
            mark_favorite_contact(contacts)
            break_action()
        elif option == 4:
            show_contacts(contacts)
            unmark_favorite_contact(contacts)
            break_action()
        elif option == 5:
            show_favorite_contacts(contacts)
            break_action()
        elif option == 6:
            show_contacts(contacts)
            delete_contact(contacts)
            break_action()
        elif option == 7:
            print("\nAté breve!")
            break
        else:
            print("Número inválido")
    except Exception as error:
        print(f"Erro no programa: {error}")

print("\nPrograma finalizado com sucesso!")