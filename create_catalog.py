
from db_config import get_connection

def create_table():
    cnx = None
    cursor = None
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        '''create_table_query = """
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
        '''

        create_table_query = """
        CREATE TABLE IF NOT EXISTS catalog (
            poi VARCHAR(150) PRIMARY KEY,
            city VARCHAR(100),
            country VARCHAR(100),
            currency VARCHAR(20),
            latitude DECIMAL(10, 6),
            longitude DECIMAL(10, 6),
            rating DECIMAL(2,1),
            description TEXT,

            spending ENUM('low', 'medium', 'high'),
            budget INT,

            vibes SET(
                'relaxed', 'adventure', 'cultural', 'nightlife',
                'nature', 'urban', 'historic', 'modern'
            ),
            activities SET(
                'museums', 'shopping', 'parks', 'architecture',
                'live music', 'sports', 'photography', 'walking tours'
            ),
            food SET(
                'coffee', 'fine dining', 'street food', 'vegetarian',
                'seafood', 'local cuisine', 'bakeries', 'brunch'
            ),

            best_season ENUM('spring', 'summer', 'fall', 'winter'),
            trip_days INT,
            nearest_airport VARCHAR(100),

            transport ENUM('walkable', 'public_transit', 'rideshare', 'car_rental'),

            accessibility TEXT,
            direction VARCHAR(500)
        );

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
