from auth.auth_service import login
from services.medicamentos import (
    cadastrar_medicamento,
    listar_medicamentos
)

def menu():
    print("\n=== FARMÁCIA SOLIDÁRIA ===")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("0 - Sair")

# ---------- LOGIN ----------
print("=== LOGIN ADMIN ===")
usuario = input("Usuário: ")
senha = input("Senha: ")

if not login(usuario, senha):
    print("Acesso negado")
    exit()

print("Login realizado com sucesso")

# ---------- MENU ----------
while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        validade = input("Validade (YYYY-MM-DD): ")
        lote = input("Lote: ")

        ok, msg = cadastrar_medicamento(
            nome, quantidade, validade, lote
        )
        print(msg)

    elif opcao == "2":
        print("\n--- MEDICAMENTOS ---")
        for m in listar_medicamentos():
            print(m)

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida")
