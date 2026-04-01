"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B1-2                                                                             *
* *
* Autor: 1681432612003 nome: Bruna Luíza Fortes Marques                             *
* Objetivo: Mostrar manipulação de lista ligada em python       *
* data: 09/03/2026                                                                           *
---------------------------------------------------------------------------------------------
"""
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.inicio = None

   
    def inserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.inicio
        self.inicio = novo
        print("Nó incluído no início com sucesso!")

    # Inserir no final
    def inserirFim(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            print("Lista estava vazia. Nó inserido no início.")
            return

        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo
        print("Nó incluído no fim com sucesso!")


    def inserirMeio(self, valor, depois_de):
        atual = self.inicio

        while atual:
            if atual.valor == depois_de:
                novo = No(valor)
                novo.proximo = atual.proximo
                atual.proximo = novo
                print("Nó inserido no meio com sucesso!")
                return
            atual = atual.proximo

        print("Valor não encontrado na lista.")

    def remover(self, valor):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.valor == valor:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                print("Nó removido com sucesso!")
                return

            anterior = atual
            atual = atual.proximo

        print("Valor não encontrado.")

   
    def buscar(self, valor):
        atual = self.inicio
        posicao = 1

        while atual:
            if atual.valor == valor:
                print(f"Valor encontrado na posição {posicao}")
                return

            atual = atual.proximo
            posicao += 1

        print("Valor não encontrado na lista.")

   
    def mostrar(self):
        atual = self.inicio

        if atual is None:
            print("Lista vazia.")
            return

        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")



lista = ListaLigada()

while True:

    print("\n**** Menu Lista Ligada ****")
    print("1. Inserir no início")
    print("2. Inserir no fim")
    print("3. Inserir após um valor (meio)")
    print("4. Remover nó")
    print("5. Buscar nó")
    print("6. Mostrar lista")
    print("7. Sair")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        valor = input("Digite o valor: ")
        lista.inserirInicio(valor)

    elif opcao == "2":
        valor = input("Digite o valor: ")
        lista.inserirFim(valor)

    elif opcao == "3":
        valor = input("Digite o novo valor: ")
        ref = input("Inserir depois de qual valor? ")
        lista.inserirMeio(valor, ref)

    elif opcao == "4":
        valor = input("Digite o valor a remover: ")
        lista.remover(valor)

    elif opcao == "5":
        valor = input("Digite o valor a buscar: ")
        lista.buscar(valor)

    elif opcao == "6":
        lista.mostrar()

    elif opcao == "7":
        print("\n**** Obrigada por usar o sistema! ****")
        print("Encerrando o sistema...")
        break

    else:
        print("Esta opção é inválida. Tente novamente.")