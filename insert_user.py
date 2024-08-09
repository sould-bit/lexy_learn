from conector_sql import connect_db
from datetime import datetime, timedelta


# Función para verificar y agregar usuario
def ensure_user_exists(user_id,user_name):
    """
    revisa en la base de datos si el usuario exite params:
    user_id = el id del usuario
    user_name = el nombre de usuario
    """
    conn = connect_db()
    cursor = conn.cursor()

    # Verificar si el usuario ya existe
    cursor.execute('SELECT COUNT(*) FROM users WHERE user_id = %s', (user_id,))
    (count,) = cursor.fetchone()

    if count == 0:
        # Si el usuario no existe, agregarlo
        cursor.execute('INSERT INTO users (user_id, username, is_premium, created_at) VALUES (%s,%s,%s,%s)', (user_id,user_name, False, datetime.now()))
        conn.commit()

    conn.close()