import psycopg2
from config import load_config


def insert_score(username, score):
    sql1 = """INSERT INTO "user"(user_name)
            VALUES(%s) RETURNING user_id;"""
    sql2 = """INSERT INTO user_score(user_id, user_score)
            VALUES(%s, %s);"""
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql1, (username,))
                rows = cur.fetchone()
                print(rows)
                if rows:
                    user_id = rows[0]

                cur.execute(sql2, (user_id, score,))
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

if __name__ == '__main__':
    insert_score(str(input()), str(input()))
       