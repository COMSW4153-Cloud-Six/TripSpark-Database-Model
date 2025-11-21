
import mysql.connector

DB_CONFIG = {
    'host': '10.142.0.4',
    'user': 'felicia',
    'password': '1234',
    'database': 'TripSparkCatalog'
}

def get_connection():
    """Establish and return a new database connection."""
    return mysql.connector.connect(**DB_CONFIG)

