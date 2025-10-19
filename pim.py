def menu():
    print("\n=== FARMÁCIA SOLIDÁRIA ===")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("4 - Requerimento de medicamento")
    print("5 - Editar medicamento")
    print("6 - Excluir medicamento")
    print("7 - Marcar medicamento como vencido")
    print("8 - Ver pilha de vencidos")
    print("0 - Sair")


def gerar_id(medicamentos):
    if len(medicamentos) == 0:
        return 1
    maior = 0
    for m in medicamentos:
        if int(m[0]) > maior:
            maior = int(m[0])
    return maior + 1

def salvar(medicamentos):
    arquivo = open("farmacia.txt", "w", encoding="utf-8")
    for m in medicamentos:
        arquivo.write(";".join(m) + "\n")
    arquivo.close()

def carregar():
    meds = []
    try:
        arquivo = open("farmacia.txt", "r", encoding="utf-8")
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 5:
                meds.append(dados)
        arquivo.close()
    except:
        pass
    return meds

def salvar_vencidos(vencidos):
    arquivo = open("vencidos.txt", "w", encoding="utf-8")
    for m in vencidos:
        arquivo.write(";".join(m) + "\n")
    arquivo.close()

def carregar_vencidos():
    pilha = []
    try:
        arquivo = open("vencidos.txt", "r", encoding="utf-8")
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 5:
                pilha.append(dados)
        arquivo.close()
    except:
        pass
    return pilha

class NoBST:
    def __init__(self, chave):
        self.chave = chave
        self.ids = []
        self.esq = None
        self.dir = None

def bst_inserir(raiz, chave, med_id):
    if raiz is None:
        n = NoBST(chave)
        n.ids.append(med_id)
        return n
    if chave == raiz.chave:
        if med_id not in raiz.ids:
            raiz.ids.append(med_id)
    elif chave < raiz.chave:
        raiz.esq = bst_inserir(raiz.esq, chave, med_id)
    else:
        raiz.dir = bst_inserir(raiz.dir, chave, med_id)
    return raiz

def bst_buscar(raiz, chave):
    if raiz is None:
        return None
    if chave == raiz.chave:
        return raiz.ids
    if chave < raiz.chave:
        return bst_buscar(raiz.esq, chave)
    return bst_buscar(raiz.dir, chave)

def construir_bst(medicamentos):
    raiz = None
    for m in medicamentos:
        chave = m[1].lower()
        med_id = int(m[0])
        raiz = bst_inserir(raiz, chave, med_id)
    return raiz

def cadastrar(medicamentos, bst_ref):
    print("\n--- Cadastro de Medicamento ---")
    nome = input("Nome: ").strip()
    quantidade = input("Quantidade: ").strip()
    validade = input("Validade: ").strip()
    lote = input("Lote: ").strip()
   
    existe = False
    for m in medicamentos:
        if m[1].lower() == nome.lower() and m[4] == lote:
            existe = True
            break
   
    if existe:
        print("Medicamento já está cadastrado.")
        return construir_bst(medicamentos)
    novo_id = str(gerar_id(medicamentos))
    registro = [novo_id, nome, quantidade, validade, lote]
    medicamentos.append(registro)
    print(f"Medicamento cadastrado. ID: {novo_id}")
    return construir_bst(medicamentos)

def listar(medicamentos):
    print("\n--- Lista de Medicamentos ---")
    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.")
    else:
        for m in medicamentos:
            print(f"ID: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]} | Lote: {m[4]}")
            try:
                if int(m[2]) <= 0:
                    print("ATENÇÃO: Estoque esgotado.")
            except:
                pass

def buscar(medicamentos, bst_ref):
    termo = input("\nDigite o nome do medicamento: ").strip().lower()
    ids = bst_buscar(bst_ref, termo)
    achou = False
    if ids:
        for m in medicamentos:
            if int(m[0]) in ids:
                print(f"ID: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]} | Lote: {m[4]}")
                achou = True
    if not achou:
        for m in medicamentos:
            if termo in m[1].lower():
                print(f"ID: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]} | Lote: {m[4]}")
                achou = True
    if not achou:
        print("Medicamento não encontrado.")


def requerimento(medicamentos):
    print("\n--- Requerimento de Medicamento ---")
    try:
        id_busca = int(input("ID do medicamento: "))
    except:
        print("ID inválido.")
        return
   
    receita = input("Número da receita: ").strip()
    qtd_txt = input("Quantidade solicitada: ").strip()
    achou = False
    for m in medicamentos:
        if int(m[0]) == id_busca:
            achou = True
            try:
                qtd_estoque = int(m[2])
                qtd_solicitada = int(qtd_txt)
            except:
                print("Quantidade inválida.")
                return
            if qtd_solicitada <= qtd_estoque:
                m[2] = str(qtd_estoque - qtd_solicitada)
                print("Requerimento registrado.")
                print(f"Medicamento {m[1]} - Receita {receita} - Quantidade retirada: {qtd_txt}")
                try:
                    if int(m[2]) == 0:
                        print("Atenção: Estoque esgotado.")
                except:
                    pass
            else:
                print("Estoque insuficiente para atender ao pedido.")
            break
   
    if not achou:
        print("Medicamento não encontrado no estoque.")

def editar(medicamentos, bst_ref):
    print("\n--- Editar Medicamento ---")
    try:
        id_busca = int(input("Digite o ID do medicamento que deseja editar: "))
    except:
        print("ID inválido.")
        return construir_bst(medicamentos)
    achou = False
    for m in medicamentos:
        if int(m[0]) == id_busca:
            achou = True
            print(f"ID: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]} | Lote: {m[4]}")
            novo_nome = input("Novo nome (Enter para manter): ").strip()
            nova_qtd = input("Nova quantidade (Enter para manter): ").strip()
            nova_validade = input("Nova validade (Enter para manter): ").strip()
            novo_lote = input("Novo lote (Enter para manter): ").strip()
            if novo_nome != "":
                m[1] = novo_nome
            if nova_qtd != "":
                m[2] = nova_qtd
            if nova_validade != "":
                m[3] = nova_validade
            if novo_lote != "":
                m[4] = novo_lote
            print("Medicamento atualizado.")
            break
    
    if not achou:
        print("Medicamento não encontrado.")
    return construir_bst(medicamentos)

def excluir(medicamentos, bst_ref):
    print("\n--- Excluir Medicamento ---")
    try:
        id_busca = int(input("Digite o ID do medicamento que deseja excluir: "))
    except:
        print("ID inválido.")
        return construir_bst(medicamentos)
    achou = False
    for i, m in enumerate(medicamentos):
        if int(m[0]) == id_busca:
            achou = True
            conf = input(f"Confirmar exclusão de {m[1]}? (s/n): ").strip().lower()
            if conf == "s":
                medicamentos.pop(i)
                print("Medicamento excluído.")
            else:
                print("Exclusão cancelada.")
            break
    if not achou:
        print("Medicamento não encontrado.")
    return construir_bst(medicamentos)

vencidos = carregar_vencidos()

def marcar_vencido(medicamentos):
    print("\n--- Marcar Medicamento como Vencido ---")
    try:
        id_busca = int(input("ID do medicamento: "))
    except:
        print("ID inválido.")
        return
    achou = False
    for i, m in enumerate(medicamentos):
        if int(m[0]) == id_busca:
            achou = True
            vencidos.append(m)
            medicamentos.pop(i)
            print("Medicamento movido para pilha de vencidos e removido do estoque.")
            break
    if not achou:
        print("Medicamento não encontrado.")

def ver_pilha_vencidos():
    print("\n--- Pilha de Vencidos (topo por último marcado) ---")
    if len(vencidos) == 0:
        print("Sem medicamentos vencidos.")
    else:
        for m in reversed(vencidos):
            print(f"ID: {m[0]} | Nome: {m[1]} | Validade: {m[3]} | Lote: {m[4]}")

medicamentos = carregar()
vencidos = carregar_vencidos()
bst = construir_bst(medicamentos)

while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        bst = cadastrar(medicamentos, bst)
    elif opcao == "2":
        listar(medicamentos)
    elif opcao == "3":
        buscar(medicamentos, bst)
    elif opcao == "4":
        requerimento(medicamentos)
    elif opcao == "5":
        bst = editar(medicamentos, bst)
    elif opcao == "6":
        bst = excluir(medicamentos, bst)
    elif opcao == "7":
        marcar_vencido(medicamentos)
        bst = construir_bst(medicamentos)
    elif opcao == "8":
        ver_pilha_vencidos()
    elif opcao == "0":
        print("Saindo...")
        salvar(medicamentos)
        salvar_vencidos(vencidos)
        break
    else:
        print("Opção inválida.")
