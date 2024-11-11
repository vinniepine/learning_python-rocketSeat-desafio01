def create_contact(contact_list):
    print("\n Por favor, insira os dados do contato:")
    contact_name = input(" Nome: ")
    contact_phone = input(" Telefone: ")
    contact_email = input(" Email: ")
    print(" Esse contato deve ser marcado como favorito?")
    favorite = input(" Digite [1] para sim ou [2] para não: ") == '1' 
    # se o usuário digitar qualquer outra coisa que não '1', favorite receberá 'False'
    # Create a dictionary for the contact
    contact = {
        "name": contact_name,
        "phone": contact_phone,
        "email": contact_email,
        "favorite": favorite
    }
    # Add the contact to the contact list
    contact_list.append(contact)
    print(f" Contato {contact_name} foi adicionado à lista.\n")
    return

def read_contacts(contact_list):
    if len(contact_list) > 0:
        print("\n\n           Lista de Contatos")
        print(    " -------------------------------------")
        for index, contact in enumerate (contact_list, start=1):
            print(" Contato n. %s" %index)
            print(" Nome: %s;" % contact["name"])
            print(" Tel.: %s;" % contact["phone"])
            print(" Email: %s;" % contact["email"])
            if contact["favorite"]:
                print(" [✔] Contato favoritado.")
            print(" -------------------------------------\n")
    else:
        print("\n Não há nenhum contato cadastrado")

def update_contact(contact_list, contact_index):
    true_index =  contact_index - 1
    if true_index >=0 and true_index < len(contact_list):
        print(" Qual dado deseja atualizar?")
        option = input(""" 
    [1] Nome
    [2] Telefone
    [3] Email
            """)
        if option == '1':
            contacts_new_name = input(" Digite o novo nome: ")
            contact_list[true_index]["name"] = contacts_new_name
        if option == '2':
            contacts_new_phone = input(" Digite o novo telefone: ")
            contact_list[true_index]["phone"] = contacts_new_phone
        if option == '3':
            contactS_new_email = input(" Digite o novo email: ")
            contact_list[true_index]["email"] = contactS_new_email
    else: 
        print("\n Índice inválido. ")
    return

def change_status(contact_list, contact_index):
    true_index = contact_index - 1
    if 0 <= true_index < len(contact_list):
        if contact_list[true_index]["favorite"]:
            favorite_status = input(""" 
 Deseja desmarcar o contato como favorito? 
   [1] Sim
   [2] Não """) != '1'
            contact_list[true_index]["favorite"] = favorite_status
        else:
            favorite_status = input(""" 
 Deseja marcar o contato como favorito? 
   [1] Sim
   [2] Não """) == '1'
            contact_list[true_index]["favorite"] = favorite_status
    else:
        print("\n Índice inválido. ")
    return

def show_favorite_contacts(contact_list):
    print("\n\n      Lista de Contatos Favoritos")
    print(" -------------------------------------")
    for index, contact in enumerate (contact_list, start=1):
        if contact["favorite"]:     
            print(" Conato n. %s" %index)
            print(" Nome: %s;" % contact["name"])
            print(" Tel.: %s;" % contact["phone"])
            print(" Email: %s;" % contact["email"])
            print(" [✔] Contato favoritado.")
            print(" -------------------------------------\n")
    return

def delete_contact(contact_list, contact_index):
    true_index = contact_index - 1
    if 0 <= true_index < len(contact_list):
        deleted_contact = contact_list.pop(true_index)
        print(f"\n Contato '{deleted_contact['name']}' foi deletado com sucesso.")
    else:
        print("\n Índice inválido. ")
    


contact_list = []
while True:
    print("\n          Agenda de contatos")
    print(" -------------------------------------")
    print(" ")
    print(" [1] Adicionar um contato;")
    print(" [2] Verificar contatos;")
    print(" [3] Editar dados de contato;")
    print(" [4] Mudar o status do contato como favorito;")
    print(" [5] Verificar contatos favoritos;")
    print(" [6] Deletar contato da lista;")
    print(" [7] Terminar aplicação")
    option = int(input("\n Por favor, digite o que deseja fazer: "))
    if option == 1:
        create_contact(contact_list)
    if option == 2:
        read_contacts(contact_list)
    if option == 3:
        index = int(input(" Qual é o índice do contato que deseja alterar? "))
        update_contact(contact_list, index)
    if option == 4:
        index = int(input(" Qual é o índice do contato que deseja alterar? "))
        change_status(contact_list, index)
    if option == 5:
        show_favorite_contacts(contact_list)
    if option == 6:
        to_be_deleted = int(input(" Digite o índice do contato que deseja deletar: "))
        delete_contact(contact_list, to_be_deleted)

    