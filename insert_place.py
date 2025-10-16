# insert_place.py
from db_config import get_connection

def insert_place(name , country , currency , lat , lon , rating_avg , description , vibe , budget , poi):
    cnx = None
    cursor = None
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        insert_query = "INSERT INTO catalog (name , country , currency , lat , lon , rating_avg , description , vibe , budget , poi) VALUES (%s, %s, %s, %d, %d, %d, %s, %s, %s, %s)"
        cursor.execute(insert_query, (name , country , currency , lat , lon , rating_avg , description , vibe , budget , poi))
        cnx.commit()

        print(f"Location '{name}' inserted successfully.")

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
    location_data = {
        "name": ["New York City", "Seattle", "New York City"],
        "country": ["USA", "USA", "USA"],
        "currency": ["USD", "USD", "USD"],
        "lat":[123243.98983, 65182736.234122, 7361265311.1231231],
        "lon":[442322334.234221, 488798712.1234234, 99893223.2355213],
        "rating_avg":[4.3, 3.5, 4.6],
        "description":["Lively place", "Good place", "Awesome place"],
        "vibe":["Good", "Bad", "Bad"],
        "budget":["$200", "$200", "$200"],
        "poi":["Times Square", "Space Needle", "Central Park"]
    }

    for i in range(3):
        insert_place(location_data["name"][i] , location_data["country"][i] , location_data["currency"][i] , location_data["lat"][i] , location_data["lon"][i] , location_data["rating_avg"][i] , location_data["description"][i] , location_data["vibe"][i] , location_data["budget"][i] , location_data["poi"][i])
