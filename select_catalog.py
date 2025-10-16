# select_catalog.py
from db_config import get_connection

def fetch_places():
    cnx = None
    cursor = None
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        select_query = "SELECT * FROM catalog"
        cursor.execute(select_query)
        results = cursor.fetchall()

        print("\nLocations in the catalog:")
        for row in results:
            print(row)

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
    fetch_places()
