import pandas as pd
from database.connection import get_connection


def exportar_estoque_csv():
    conexao = get_connection()
    query = """
        SELECT nome, quantidade, validade, lote
        FROM medicamentos
        WHERE ativo = 1
    """
    df = pd.read_sql(query, conexao)
    df.to_csv("estoque_atual.csv", index=False)
    conexao.close()
