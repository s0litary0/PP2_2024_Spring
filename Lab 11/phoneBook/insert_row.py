import psycopg2
import csv
from config import load_config


def insert_number(phone_number, name, address):
    """Insert a new phone number into the names and addresses tables"""

    sql1 = """INSERT INTO names(phone_number, name)
            VALUES(%s, %s);"""
    sql2 = """INSERT INTO addresses(phone_number, address)
            VALUES(%s, %s);"""
    config = load_config()
    tuple = ((phone_number, name), (phone_number, address), )
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql1, tuple[0])
                cur.execute(sql2, tuple[1])
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    
def insert_number_from_csv(file_name):
    """ Insert a new phone number from csv file into the names and addresses tables"""

    with open("phone_book_file.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    print(data)

    sql1 = """INSERT INTO names(phone_number, name)
            VALUES(%s, %s);"""
    sql2 = """INSERT INTO addresses(phone_number, address)
            VALUES(%s, %s);"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                for x in data:
                    cur.execute(sql1, (x['phone_number'], x['name'], ))
                    cur.execute(sql2, (x['phone_number'], x['address'], ))
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    while True:
        print("Choose way to add data:\n1 - terminal input\n2 - csv file\nPress any other key to exit")
        way = int(input())
        if way == 1:
            insert_number(str(input()), str(input()), str(input()))
        if way == 2:
            insert_number_from_csv("phone_book_file.csv")
        else:
            break