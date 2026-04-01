
"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B1-1                                                                             *
* *
* Autor: 1681432612003 nome: Bruna Luíza Fortes Marques                             *
* Objetivo: Criação de um sistema com menu em que funcionem as funcionalidades de: Inserir, Consultar, Buscar,
 Remover e Listar filmes. O Acesso a essas funcionalidades deve ser através de um menu.          *
* data: 01/03/2026                                                                           *
---------------------------------------------------------------------------------------------
"""
catalogo = {}

def adicionar_filme():
    """Insere um novo filme se o ID nao existir."""
    
    print("\n**** Inserir novo filme ****")
    id_filme = input("Digite o id do filme: ")

    if id_filme in catalogo:
        print("Este filme já existe no nosso catálogo")
    else:
        print("\n**** Insira o novo filme ****")
        titulo = input("Por favor digite o título do filme a adicionar: ")
        diretor = input("Por favor digite o diretor do filme a adicionar: ")
        catalogo[id_filme] = {'titulo': titulo, 'diretor': diretor}

        print(f"O Filme {titulo} dirigido por {diretor}, foi inserido com sucesso no catálogo")


def buscar_filme():
    """Consulta um filme usando o método seguro .get()"""

    print("\n**** Buscar um filme no catálogo ****")
    id_filme = input("Por favor digite o ID do filme para a busca: ")
    filme = catalogo.get(id_filme)

    if filme:
        print("\nO filme está no catálogo:")
        print(f"\nID do filme: {id_filme}")
        print(f"Título do filme: {filme['titulo']}")
        print(f"Diretor do filme: {filme['diretor']}")
    else:
        print("Filme não disponível no catálogo")


def remover_filme():
    """Remove um filme do dicionario usando .pop()."""

    print("\n**** Remover um filme ****")
    id_filme = input("Por favor digite o ID do filme que deseja excluir: ")
    excluido = catalogo.pop(id_filme, None)

    if excluido:
        print("O filme foi removido com sucesso de nosso catálogo!")
    else:
        print("O ID do filme não foi encontrado.")


def listar_todos():
    """Itera sobre os itens do dicionário para listagem."""

    if not catalogo:
        print("\nO catálogo esta vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_filme, dados in catalogo.items():
            print(f"ID: {id_filme} | Titulo: {dados['titulo']} "
                  f"| Diretor: {dados['diretor']}")


def menu():
    while True:
        print("\n**** Menu sistema de filmes ****")
        print("1. Adicionar")
        print("2. Buscar")
        print("3. Remover")
        print("4. Listar")
        print("5. Sair")

        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            adicionar_filme()

        elif opcao == "2":
            buscar_filme()

        elif opcao == "3":
            remover_filme()

        elif opcao == "4":
            listar_todos()

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Esta opção é inválida. Tente mais uma vez.")


menu()