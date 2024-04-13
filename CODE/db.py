import psycopg

DB_NAME = "HealthFitnessClub"
DB_USER = "postgres"
DB_PASS = ""
DB_HOST = "localhost"

def connect_db():
    """Connect to the PostgreSQL database. Returns a connection object."""
    try:
        conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        return conn
    except psycopg.DatabaseError as e:
        print(f"An error occurred while connecting to the database: {e}")
        exit(1)