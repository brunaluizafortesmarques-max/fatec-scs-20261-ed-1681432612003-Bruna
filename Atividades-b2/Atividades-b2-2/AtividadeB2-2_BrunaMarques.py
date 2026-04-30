fila_adm = []
fila_alunos = []
fila_impressao = []

def adicionar_documento():
    print("\nAdicione um documento")
    nome = input("Qual o nome do arquivo? ")
    paginas = int(input("Quantas páginas tem? "))
    
    documento = {"nome": nome, "paginas": paginas}
    
    while True:
        tipo = input("É da administração ou aluno? (adm/aluno): ").lower()
        
        if tipo == "adm":
            fila_adm.append(documento)
            print(f"Perfeito! '{nome}' foi para a fila da administração!")
            break
        elif tipo == "aluno":
            fila_alunos.append(documento)
            print(f"Ótimo! '{nome}' foi para a fila dos alunos.")
            break
        else:
            print("Desculpe, só é aceito 'adm' ou 'aluno'. Tente de novo!")

def reorganizar_fila():
    print("\nPreparando a fila de impressão...")
    
    if fila_impressao:
        print("A impressora já tem documentos na fila!")
        return
    
    fila_impressao.extend(fila_adm)
    fila_impressao.extend(fila_alunos)
    
    fila_adm.clear()
    fila_alunos.clear()
    
    print("Tudo pronto! Fila organizada.")

def consumir_fila():
    if not fila_impressao:
        print("Nada para imprimir no momento.")
        return
    
    documento = fila_impressao.pop(0)
    print(f"\nImprimindo agora: '{documento['nome']}'")
    print(f"Total de páginas: {documento['paginas']}")
    print("Impressão concluída com sucesso! ")

def listar_filas():
    print("\n--- Status das filas ---")
    
    print("Fila da Administração:", end=" ")
    if not fila_adm:
        print("vazia")
    else:
        for i, doc in enumerate(fila_adm, 1):
            print(f"{i}. {doc['nome']}", end=" ")
    
    print("\nFila dos Alunos:", end=" ")
    if not fila_alunos:
        print("vazia")
    else:
        for i, doc in enumerate(fila_alunos, 1):
            print(f"{i}. {doc['nome']}", end=" ")
    
    print("\nFila da Impressora:", end=" ")
    if not fila_impressao:
        print("vazia")
    else:
        for i, doc in enumerate(fila_impressao, 1):
            print(f"{i}. {doc['nome']}", end=" ")
    print()

def menu():
    while True:
        print("\n=== MENU DA IMPRESSORA ===")
        print("1. Adicionar documento")
        print("2. Reorganizar fila")
        print("3. Consumir fila (imprimir)")
        print("4. Listar filas")
        print("5. Sair")
        
        opcao = input("O que você quer fazer? Selecione uma das opções de 1-5: ")
        
        if opcao == "1":
            adicionar_documento()
        elif opcao == "2":
            reorganizar_fila()
        elif opcao == "3":
            consumir_fila()
        elif opcao == "4":
            listar_filas()
        elif opcao == "5":
            print("\nObrigada por usar a impressora.")
            break
        else:
            print("Opção inválida! Digite uma opção de 1 a 5.")

menu()