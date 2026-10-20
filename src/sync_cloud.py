import psycopg2

def probar_conexion_local():
    try:
        conn = psycopg2.connect(
            dbname="df_p01_db",
            user="postgres",
            password="Juliana",
            host="localhost",
            port="5432"
        )
        print("Conexión exitosa a PostgreSQL local")
        conn.close()
    except Exception as e:
        print(f"Error al conectar a PostgreSQL: {e}")

if __name__ == "__main__":
    probar_conexion_local()
     