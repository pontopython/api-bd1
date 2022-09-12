def create_user_dict(id, name, email, password):                    # CRIA O DICIONÁRIO DE CADA USUÁRIO
    
    return {
        "id": id,
        "name": name,
        "email": email,
        "password": password,
    }

def line_to_user_dict(line):                                        # TRANSFORMA UMA STRING EM UM DICIONÁRIO DE USUÁRIO
    splitted_line = line.split(";")                                 # transforma a string em um array, e separa os elementos pelo ";"
    id = int(splitted_line[0])
    name = splitted_line[1]
    email = splitted_line[2]
    password = splitted_line[3]
    password = password[:-1]                                        # retira o \n do final do password, para gerar uma lista precisa***

    return create_user_dict(id, name, email, password)              # com os parâmetros definidos, retorna a criação do dicionário

def generate_users_list():                                          # CRIA A LISTA DE USUÁRIOS BASEADO NO ARQUIVO USERS.TXT
    file = open("data/users.txt", "r")
    users_list = []                                                 # inicializa uma lista vazia
    for line in file:                                               # para cada linha do arquivo USERS.TXT
        user = line_to_user_dict(line)                              # transforma a linha de string para dicionário
        users_list.append(user)                                     # adiciona ao final da lista criada anteriormente
    file.close()
    # --OPCIONAL--
    return display_users_list(users_list)                           # retorna e aciona o display da lista no console

    # --OPCIONAL--
def display_users_list(users_list):                                 # ESCREVE A LISTA DE USUÁRIOS NO CONSOLEx
    for x in users_list:
        print(x)

    return

# TESTE COM SAMPLE EM USERS.TXT
if __name__ == "__main__":
    print('MAIN MENU')
    print('1 - Generate and display users list')
    print('2 - Close')
    option = int(input('Choose one option: '))
    if option == 1:
        generate_users_list()
    elif option == 2:
        print('Bye bye!')
    else:
        print('Opção inválida!')