from auth.auth_service import login
from services.medicamentos import cadastrar_medicamento, listar_medicamentos
from services.movimentacoes import registrar_entrada, registrar_saida
from services.controle_vencimento import verificar_medicamentos_vencidos


def menu():
    print("\n=== FARMÁCIA SOLIDÁRIA ===")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Verificar vencidos")
    print("0 - Sair")


def sistema():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome: ")
                quantidade = int(input("Quantidade: "))
                validade = input("Validade (AAAA-MM-DD): ")
                lote = input("Lote: ")

                cadastrar_medicamento(nome, quantidade, validade, lote)
                print("Medicamento cadastrado com sucesso.")

            elif opcao == "2":
                medicamentos = listar_medicamentos()
                for m in medicamentos:
                    print(
                        f"ID: {m['id']} | {m['nome']} | "
                        f"Qtd: {m['quantidade']} | Validade: {m['validade']}"
                    )

            elif opcao == "3":
                med_id = int(input("ID do medicamento: "))
                qtd = int(input("Quantidade: "))
                obs = input("Observação: ")
                registrar_entrada(med_id, qtd, obs)
                print("Entrada registrada.")

            elif opcao == "4":
                med_id = int(input("ID do medicamento: "))
                qtd = int(input("Quantidade: "))
                obs = input("Observação: ")
                registrar_saida(med_id, qtd, obs)
                print("Saída registrada.")

            elif opcao == "5":
                verificar_medicamentos_vencidos()
                print("Verificação concluída.")

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)


def main():
    print("=== LOGIN ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if login(usuario, senha):
        print("Login realizado com sucesso.")
        sistema()
    else:
        print("Usuário ou senha inválidos.")


if __name__ == "__main__":
    main()
