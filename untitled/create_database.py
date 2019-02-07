from models import Client,Order,Product
from psycopg2 import OperationalError
from psql_connection import make_connection


if __name__ == "__main__":

    try:
        connection = make_connection()
        cursor = connection.cursor()
        cursor.execute(Client.generate_create_sql())
        cursor.execute(Order.generate_create_sql())
        cursor.execute(Product.generate_create_sql())
        cursor.close()
        connection.close()
    except OperationalError as oe:
        print (oe)
    except Exception as e:
        print(e)