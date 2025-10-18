def menu():
    print("\n=== FARMÁCIA SOLIDÁRIA ===")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("4 - Requerimento de medicamento")
    print("0 - Sair")

def cadastrar(medicamentos):
    print("\n--- Cadastro de Medicamento ---")
    codigo = input("Código: ")
    nome = input("Nome: ")
    quantidade = input("Quantidade: ")
    validade = input("Validade: ")
    lote = input("Lote: ")
    medicamento = [codigo, nome, quantidade, validade, lote]
    medicamentos.append(medicamento)
    print("Medicamento cadastrado com sucesso.")

def listar(medicamentos):
    print("\n--- Lista de Medicamentos ---")
    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.")
    else:
        for m in medicamentos:
            print(f"Código: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]} | Lote: {m[4]}")

def buscar(medicamentos):
    nome = input("\nDigite o nome do medicamento: ").lower()
    achou = False
    for m in medicamentos:
        if nome in m[1].lower():
            print(f"Código: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]} | Lote: {m[4]}")
            achou = True
    if not achou:
        print("Medicamento não encontrado.")

def requerimento(medicamentos):
    print("\n--- Requerimento de Medicamento ---")
    nome = input("Nome do medicamento: ").lower()
    receita = input("Número da receita: ")
    achou = False
    for m in medicamentos:
        if nome in m[1].lower():
            print(f"Medicamento {m[1]} encontrado.")
            print(f"Requerimento registrado para a receita {receita}.")
            achou = True
            break
    if not achou:
        print("Medicamento não encontrado no estoque.")

def salvar(medicamentos):
    arquivo = open("farmacia.txt", "w")
    for m in medicamentos:
        linha = ";".join(m) + "\n"
        arquivo.write(linha)
    arquivo.close()

def carregar():
    medicamentos = []
    try:
        arquivo = open("farmacia.txt", "r")
        for linha in arquivo:
            dados = linha.strip().split(";")
            medicamentos.append(dados)
        arquivo.close()
    except:
        pass
    return medicamentos

medicamentos = carregar()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar(medicamentos)
    elif opcao == "2":
        listar(medicamentos)
    elif opcao == "3":
        buscar(medicamentos)
    elif opcao == "4":
        requerimento(medicamentos)
    elif opcao == "0":
        print("Saindo...")
        salvar(medicamentos)
        break
    else:
        print("Opção inválida.")