from datetime import date
from database.connection import get_connection

def verificar_medicamentos_vencidos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    hoje = date.today()

    cursor.execute("""
        SELECT * FROM medicamentos
        WHERE validade < %s AND ativo = 1
    """, (hoje,))

    vencidos = cursor.fetchall()

    for med in vencidos:
        print("Inserindo vencido:", med["nome"])
        # Insere na tabela de vencidos
        cursor.execute("""
            INSERT INTO medicamentos_vencidos
            (nome, quantidade, data_validade, data_movimentacao, motivo)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            med["nome"],
            med["quantidade"],
            med["validade"],
            hoje,
            "VENCIMENTO"
        ))

        # Marca como inativo
        cursor.execute("""
            UPDATE medicamentos
            SET ativo = 0
            WHERE id = %s
        """, (med["id"],))

        print("Total vencidos encontrados:", len(vencidos))

    conn.commit()
    cursor.close()
    conn.close()
