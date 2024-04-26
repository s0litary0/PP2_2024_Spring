import psycopg2
from config import load_config


def delete_phone_number(name, address):
    """ Delete phone_number by address and name """

    rows_deleted  = 0
    sql1 = 'DELETE FROM names WHERE name = %s'
    sql2 = 'DELETE FROM addresses WHERE address = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql1, (name,))
                cur.execute(sql2, (address,))

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

if __name__ == '__main__':
    delete_phone_number(input(), input())
