import psycopg2
from config import load_config


def get_name_by_number(number):
    """ Get parts provided by a vendor specified by the vendor_id """
    records = []
    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                cur.callproc('get_name_by_number', (number,))
                
                # process the result set
                row = cur.fetchone()
                while row is not None:
                    records.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return records

if __name__ == '__main__':
    records = get_name_by_number(input())
    print(records)