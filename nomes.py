# Lendo e escrevendo arquivos com python (exemplo inicial)

nome_do_arquivo = 'data/nomes.txt'


def extrair_nomes():
    arquivo = open(nome_do_arquivo, 'r')        # Abre o arquivo para leitura (r de read)
    nomes = []                                  # Cria lista de nomes, inicialmente vazia
    for linha in arquivo:                       # Repete instruções abaixo para cada linha do arquivo
        nomes.append(linha.replace("\n", ""))   # Remove "nova linha" da string e adiciona na lista
    arquivo.close()                             # fecha o arquivo para que outro programa possa voltar a usar
    return nomes                                # lista com os nomes será o valor retornado pela função/método extrair_nomes()


def salvar_novo_nome(novo_nome):
    arquivo = open(nome_do_arquivo, 'a')        # Abre o arquivo para acrescentar algo no final (a de append)
    arquivo.write("\n")                         # Adiciona nova linha no arquivo
    arquivo.write(novo_nome)                    # Adiciona o nome na nova linha
    arquivo.close()                             # fecha o arquivo para que outro programa possa voltar a usar


if __name__ == "__main__":
    while True:                                 # Repete instruções abaixo "pra sempre"
        print()                                 # Escreve uma linha em branco (para espaçamento)
        print("Menu")
        print("1 - Listar Nomes")
        print("2 - Salvar Novo Nome")
        print("3 - Sair")

        opcao = int(input("Opção: "))
        print()                                 # Escreve uma linha em branco (para espaçamento)

        if opcao == 1:
            nomes = extrair_nomes()
            for nome in nomes:
                print(nome)
        elif opcao == 2:
            novo_nome = input("Digite o novo nome a ser salvo: ")
            salvar_novo_nome(novo_nome)
        elif opcao == 3:                        # Opção Sair
            break                               # Break sai do loop e encerra o programa
        else:
            print("Opção Inválida")
