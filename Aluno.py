alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    numero = input("Digite o número do aluno: ")
    aluno = {"nome": nome, "numero": numero}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def atualizar_aluno():
    numero = input("Digite o número do aluno que deseja atualizar: ")
    for aluno in alunos:
        if aluno["numero"] == numero:
            novo_nome = input("Digite o novo nome do aluno: ")
            aluno["nome"] = novo_nome
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def deletar_aluno():
    numero = input("Digite o número do aluno que deseja deletar: ")
    for aluno in alunos:
        if aluno["numero"] == numero:
            alunos.remove(aluno)
            print("Aluno deletado com sucesso!")
            return
    print("Aluno não encontrado.")

def pesquisar_aluno():
    numero = input("Digite o número do aluno que deseja pesquisar: ")
    for aluno in alunos:
        if aluno["numero"] == numero:
            print(f"Nome do aluno: {aluno['nome']}")
            return
    print("Aluno não encontrado.")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nTabela de Alunos:")
        print("{:<15} {:<10}".format("Nome", "Número"))
        print("-" * 25)
        for aluno in alunos:
            print("{:<15} {:<10}".format(aluno["nome"], aluno["numero"]))

while True:
    print("\nMenu:")
    print("1. Cadastrar aluno")
    print("2. Atualizar aluno")
    print("3. Deletar aluno")
    print("4. Pesquisar aluno")
    print("5. Listar alunos")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        atualizar_aluno()
    elif opcao == '3':
        deletar_aluno()
    elif opcao == '4':
        pesquisar_aluno()
    elif opcao == '5':
        listar_alunos()
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")