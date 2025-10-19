def menu():
    print("\n=== FARMÁCIA SOLIDÁRIA ===")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("4 - Requerimento de medicamento")
    print("5 - Editar medicamento")
    print("6 - Excluir medicamento")
    print("0 - Sair")


def gerar_id(medicamentos):
    if len(medicamentos) == 0:
        return 1
    maior_id = 0
    for m in medicamentos:
        try:
            valor = int(m[0])
            if valor > maior_id:
                maior_id = valor
        except:
            pass
    return maior_id + 1


def cadastrar(medicamentos):
    print("\n--- Cadastro de Medicamento ---")
    nome = input("Nome: ").strip()
    quantidade = input("Quantidade: ").strip()
    validade = input("Validade: ").strip()
    lote = input("Lote: ").strip()

    try:
        qtd_int = int(quantidade)
        if qtd_int < 0:
            print("Quantidade inválida.")
            return
    except:
        print("Quantidade inválida.")
        return

    existe = False
    for m in medicamentos:
        if m[1].lower() == nome.lower() and m[4] == lote:
            existe = True
            break

    if existe:
        print("Medicamento já está cadastrado.")
    else:
        novo_id = str(gerar_id(medicamentos))
        novo = [novo_id, nome, str(qtd_int), validade, lote]
        medicamentos.append(novo)
        print("Medicamento cadastrado com sucesso. ID:", novo_id)


def listar(medicamentos):
    print("\n--- Lista de Medicamentos ---")
    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.")
    else:
        for m in medicamentos:
            print("Código:", m[0], "| Nome:", m[1], "| Qtd:", m[2], "| Validade:", m[3], "| Lote:", m[4])


def buscar(medicamentos):
    nome = input("\nDigite o nome do medicamento: ").strip().lower()
    achou = False
    for m in medicamentos:
        if nome in m[1].lower():
            print("Código:", m[0], "| Nome:", m[1], "| Qtd:", m[2], "| Validade:", m[3], "| Lote:", m[4])
            achou = True
    if not achou:
        print("Medicamento não encontrado.")


def requerimento(medicamentos):
    print("\n--- Requerimento de Medicamento ---")
    try:
        id_busca = int(input("ID do medicamento: ").strip())
    except:
        print("ID inválido.")
        return

    receita = input("Número da receita: ").strip()
    try:
        quantidade = int(input("Quantidade solicitada: ").strip())
        if quantidade <= 0:
            print("Quantidade inválida.")
            return
    except:
        print("Quantidade inválida.")
        return

    achou = False
    for m in medicamentos:
        if int(m[0]) == id_busca:
            achou = True
            try:
                qtd_estoque = int(m[2])
            except:
                qtd_estoque = 0

            if quantidade <= qtd_estoque:
                m[2] = str(qtd_estoque - quantidade)
                print("Requerimento registrado.")
                print("Medicamento:", m[1], "- Receita:", receita, "- Quantidade:", quantidade)
                if int(m[2]) == 0:
                    print("ATENÇÃO: Medicamento em falta no estoque!")
            else:
                print("Estoque insuficiente para atender ao pedido.")
            break

    if not achou:
        print("Medicamento não encontrado.")


def editar(medicamentos):
    print("\n--- Edição de Medicamento ---")
    try:
        id_busca = int(input("Digite o ID do medicamento que deseja editar: ").strip())
    except:
        print("ID inválido.")
        return

    achou = False
    for m in medicamentos:
        if int(m[0]) == id_busca:
            achou = True
            print("Medicamento encontrado:", m[1])
            print("ID:", m[0], "| Nome:", m[1], "| Quantidade:", m[2], "| Validade:", m[3], "| Lote:", m[4])

            nome = input("Novo nome (deixe em branco para manter): ").strip()
            quantidade = input("Nova quantidade (deixe em branco para manter): ").strip()
            validade = input("Nova validade (deixe em branco para manter): ").strip()
            lote = input("Novo lote (deixe em branco para manter): ").strip()

            if nome != "":
                m[1] = nome
            if quantidade != "":
                try:
                    qtd_int = int(quantidade)
                    if qtd_int >= 0:
                        m[2] = str(qtd_int)
                    else:
                        print("Quantidade inválida. Mantendo valor anterior.")
                except:
                    print("Quantidade inválida. Mantendo valor anterior.")
            if validade != "":
                m[3] = validade
            if lote != "":
                m[4] = lote

            print("Medicamento atualizado com sucesso.")
            break

    if not achou:
        print("Medicamento não encontrado.")


def excluir(medicamentos):
    print("\n--- Excluir Medicamento ---")
    try:
        id_busca = int(input("Digite o ID do medicamento que deseja excluir: ").strip())
    except:
        print("ID inválido.")
        return

    achou = False
    for i, m in enumerate(medicamentos):
        if int(m[0]) == id_busca:
            achou = True
            confirmacao = input("Tem certeza que deseja excluir o medicamento " + m[1] + "? (s/n): ").strip().lower()
            if confirmacao == 's':
                medicamentos.pop(i)
                print("Medicamento excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            break
    if not achou:
        print("Medicamento não encontrado.")


def main():
    medicamentos = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(medicamentos)
        elif opcao == "2":
            listar(medicamentos)
        elif opcao == "3":
            buscar(medicamentos)
        elif opcao == "4":
            requerimento(medicamentos)
        elif opcao == "5":
            editar(medicamentos)
        elif opcao == "6":
            excluir(medicamentos)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
