from database.connection import get_connection
from datetime import date

def registrar_entrada(medicamento_id, quantidade, observacao=None):
    conexao = get_connection()
    cursor = conexao.cursor()

    # atualiza estoque
    cursor.execute("""
        UPDATE medicamentos
        SET quantidade = quantidade + %s
        WHERE id = %s AND ativo = 1
    """, (quantidade, medicamento_id))

    # registra movimentação
    cursor.execute("""
        INSERT INTO movimentacoes_estoque
        (medicamento_id, tipo, quantidade, data_movimentacao, observacao)
        VALUES (%s, 'ENTRADA', %s, %s, %s)
    """, (medicamento_id, quantidade, date.today(), observacao))

    conexao.commit()
    cursor.close()
    conexao.close()

def registrar_saida(medicamento_id, quantidade, observacao=None):
    conexao = get_connection()
    cursor = conexao.cursor()

    # verifica estoque
    cursor.execute("""
        SELECT quantidade FROM medicamentos
        WHERE id = %s AND ativo = 1
    """, (medicamento_id,))
    
    resultado = cursor.fetchone()

    if not resultado:
        cursor.close()
        conexao.close()
        raise Exception("Medicamento não encontrado ou inativo.")

    estoque_atual = resultado[0]

    if quantidade > estoque_atual:
        cursor.close()
        conexao.close()
        raise Exception("Quantidade insuficiente em estoque.")

    # atualiza estoque
    cursor.execute("""
        UPDATE medicamentos
        SET quantidade = quantidade - %s
        WHERE id = %s
    """, (quantidade, medicamento_id))

    # registra movimentação
    cursor.execute("""
        INSERT INTO movimentacoes_estoque
        (medicamento_id, tipo, quantidade, data_movimentacao, observacao)
        VALUES (%s, 'SAIDA', %s, %s, %s)
    """, (medicamento_id, quantidade, date.today(), observacao))

    conexao.commit()
    cursor.close()
    conexao.close()
