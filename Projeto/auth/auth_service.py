from database.connection import get_connection
import hashlib

def login(username, password):
    senha_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE username = %s AND senha = %s",
        (username, senha_hash)
    )

    usuario = cursor.fetchone()
    conn.close()

    return usuario is not None
