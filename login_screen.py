from pickle import TRUE
from utils import bright_print
import stdiomask
from create_save import line_to_user_dict


def create_login_dict(id, category, name, email, password):      
    return {
        "id": id,
        "category": category,
        "name": name,
        "email": email,
        "password": password,
    }

def log_dict_to_line(user):
    id = user["id"]
    category = user["category"]
    name = user["name"]
    email = user["email"]

    return f"{id};{category};{name};{email}"


def line_to_login_dict(line):                          
    splitted_line = line.split(";")                   
    id = splitted_line[0]
    category = splitted_line[1]
    name = splitted_line[2]
    email = splitted_line[3]
    password = splitted_line[4]
    password = password[:-1]                          
    return create_login_dict(id, category, name, email, password)


#Formulário_Login
def login_user():
    bright_print("\nLogin do Usuário\n")
    login = input('Usuário:')
    password = stdiomask.getpass(prompt='Senha:', mask="*")
    
    return login, password


#Verificação_Existência_Usuário_Na_Base
def search_user_by_email(login):
    file = open('data/users.txt', 'r')
    ver = False
    
    while ver != TRUE:

        for line in file:
            user = line_to_login_dict(line)
            
            if login == user['email']:
                return user
              
        break
    file.close()
    
    return


#Validação_das_Credenciais
def Credential_Validation(user, password):
    
    if user is not None and password == user['password']:
        return False
    
    else:
        print('Credenciais Inválidas!')


#Registro_do_Log
def access_log(user):
    file = open('data/register_log.txt', 'a')
    line = log_dict_to_line(user)
    file.write(line)
    file.write('\n')
    file.close()
    



if __name__ == "__main__":

    login, password = login_user()
    user = search_user_by_email(login)
    if Credential_Validation(user, password) == False:
        access_log(user)


    
