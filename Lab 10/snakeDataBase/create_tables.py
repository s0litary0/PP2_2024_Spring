import psycopg2
from config import load_config

def create_tables():
    """ Create table in the PostgreSQL database"""
    commands = (
        """CREATE TABLE "user" (
            "user_id" SERIAL PRIMARY KEY,
            "user_name" VARCHAR(255) NOT NULL
        )
        """, 
        """CREATE TABLE user_score (
            "user_id" INTEGER PRIMARY KEY,
            "user_score" INTEGER,
            FOREIGN KEY ("user_id")
                REFERENCES "user" ("user_id")
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