# create_catalog.py
from db_config import get_connection

def create_table():
    cnx = None
    cursor = None
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS catalog (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            country VARCHAR(64) NOT NULL,
            currency VARCHAR(8),
            lat DECIMAL(9,6), 
            lon DECIMAL(9,6),
            rating_avg DECIMAL(2,1),
            description TEXT,
            vibe VARCHAR(50),
            budget VARCHAR(50),
            poi VARCHAR(50)
        )
        """
        cursor.execute(create_table_query)
        print("Table 'catalog' created or already exists.")

    except Exception as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass

        if cnx and cnx.is_connected():
            try:
                cnx.close()
                print("MySQL connection closed.")
            except Exception:
                pass

if __name__ == "__main__":
    create_table()
