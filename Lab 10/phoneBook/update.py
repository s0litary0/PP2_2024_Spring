import psycopg2
from config import load_config


def update_phone_number(phone_number, name):
    """ Update phone number based on the name """

    sql = """
        UPDATE names
            SET phone_number = %s
            WHERE name = %s
        """
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (phone_number, name,))

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

if __name__ == '__main__':
    while True:
        print("Update data:\n1 - terminal input\nPress any other key to exit")
        way = int(input())
        if way == 1:
            update_phone_number(str(input("Enter phone number: ")), str(input("Enter name: ")))
        else:
            break