import mysql.connector

DB_CONFIG = {
    'host': 'your_ec2_instance_public_ip',  # or private IP if in same VPC
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database_name'
}

def get_connection():
    """Establish and return a new database connection."""
    return mysql.connector.connect(**DB_CONFIG)