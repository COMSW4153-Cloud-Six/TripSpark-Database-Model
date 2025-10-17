
# GCP VM

import sqlalchemy
from google.cloud.sql.connector import Connector, IPTypes
from google.auth.exceptions import DefaultCredentialsError

# Environment variables
INSTANCE_CONNECTION_NAME = "INSTANCE_CONNECTION_NAME"
DB_USER = "DB_USER"
DB_PASS = "DB_PASS"
DB_NAME = "DB_NAME"

connector = None
engine = None

try:
        connector = Connector()
        print("I'm done")

        def get_conn():
            conn = connector.connect(
                INSTANCE_CONNECTION_NAME,
                "pymysql",
                user=DB_USER,
                password=DB_PASS,
                db=DB_NAME,
                ip_type=IPTypes.PUBLIC,
            )

            return conn

        # Create SQLAlchemy engine
        engine = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=get_conn
        )

        print("Cloud SQL connector initialized successfully.")

except DefaultCredentialsError:
        print("Failed to find Google Cloud credentials.")
        print(
            "Run `gcloud auth application-default login` or set the GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        engine = None

except Exception as e:
        print("Unexpected error initializing connector:")
        print(e)
        engine = None



''' AWS VM
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
'''
