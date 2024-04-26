import psycopg2
from config import load_config

def create_tables():
    """ Create table in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE names(
            Phone_number VARCHAR(10) PRIMARY KEY,
            Name VARCHAR(255) NOT NULL
        )
        """, 
        """
        CREATE TABLE addresses(
            Phone_number VARCHAR(10) PRIMARY KEY,
            Address VARCHAR(255) NOT NULL,
            FOREIGN KEY (Phone_number)
                REFERENCES names (Phone_number)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()