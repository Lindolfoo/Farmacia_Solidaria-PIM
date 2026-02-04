from database.connection import get_connection
from utils.dates import str_para_data, dias_para_vencer
from database.connection import get_connection

def cadastrar_medicamento(nome, quantidade, validade_str, lote):
    validade = str_para_data(validade_str)

    if dias_para_vencer(validade) < 0:
        return False, "Não é possível cadastrar medicamento vencido."

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id FROM medicamentos WHERE nome=%s AND lote=%s",
        (nome, lote)
    )

    if cursor.fetchone():
        conn.close()
        return False, "Medicamento já cadastrado"

    cursor.execute(
        """
        INSERT INTO medicamentos (nome, quantidade, validade, lote)
        VALUES (%s, %s, %s, %s)
        """,
        (nome, quantidade, validade, lote)
    )

    conn.commit()
    conn.close()
    return True, "Medicamento cadastrado"


def listar_medicamentos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM medicamentos")
    dados = cursor.fetchall()

    conn.close()
    return dados

def buscar_medicamento(nome_busca):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, nome, quantidade, validade, lote
        FROM medicamentos
        WHERE ativo = 1 AND nome LIKE %s
    """, (f"%{nome_busca}%",))

    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado
