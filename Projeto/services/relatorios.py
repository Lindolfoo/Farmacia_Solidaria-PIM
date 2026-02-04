from database.connection import get_connection

def relatorio_estoque():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, nome, quantidade, validade, lote
        FROM medicamentos
        WHERE ativo = 1
        ORDER BY validade
    """)

    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados


def relatorio_movimentacoes():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT m.nome,
               me.tipo,
               me.quantidade,
               me.data_movimentacao,
               me.observacao
        FROM movimentacoes_estoque me
        JOIN medicamentos m ON m.id = me.medicamento_id
        ORDER BY me.data_movimentacao DESC
    """)

    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados


def relatorio_vencidos():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT nome, quantidade, data_validade, data_movimentacao, motivo
        FROM medicamentos_vencidos
        ORDER BY data_movimentacao DESC
    """)

    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados
