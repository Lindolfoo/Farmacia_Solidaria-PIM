from auth.auth_service import login
from services.medicamentos import cadastrar_medicamento, listar_medicamentos
from services.movimentacoes import registrar_entrada, registrar_saida
from services.controle_vencimento import verificar_medicamentos_vencidos
from services.exportacao import exportar_estoque_csv
from services.relatorios import (
    relatorio_estoque,
    relatorio_movimentacoes,
    relatorio_vencidos
)
from services.medicamentos import (
    cadastrar_medicamento,
    listar_medicamentos,
    buscar_medicamento
)

def menu():
    print("\n=== FARMÁCIA SOLIDÁRIA ===")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Verificar vencidos")
    print("6 - Relatório de estoque")
    print("7 - Relatório de movimentações")
    print("8 - Relatório de vencidos")
    print("9 - Buscar medicamento por nome")
    print("10 - Exportar estoque para CSV")
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

            elif opcao == "6":
                for r in relatorio_estoque():
                    print(r)

            elif opcao == "7":
                for r in relatorio_movimentacoes():
                    print(r)

            elif opcao == "8":
                for r in relatorio_vencidos():
                    print(r)

            elif opcao == "9":
                termo = input("Digite o nome do medicamento: ")
                resultados = buscar_medicamento(termo)

                if not resultados:
                    print("Nenhum medicamento encontrado.")
                else:
                    for r in resultados:
                        print(r)

            elif opcao == "10":
                exportar_estoque_csv()
                print("Arquivo estoque_atual.csv gerado com sucesso.")


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
