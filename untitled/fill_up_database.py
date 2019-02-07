from models import Client, Order, Product
from psycopg2 import OperationalError
from psql_connection import make_connection


def generate_query(item):
    column_names = list(item['fields'].keys())
    sql = f"INSERT INTO {item['table_name']} ("
    names = []
    for column in column_names:
        names.append(f"{column}")
    sql += ','.join(names)
    sql += ") VALUES ("
    names = []
    for column in column_names:
        names.append(f"'{item['fields'][column]}'")
    sql += ','.join(names)
    sql += ");"
    return sql


def add_item_to_db(cursor, item):
    sql = generate_query(item.create_dictionary())
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)


if "__main__" == __name__:
    items = [Product(name="Mleko", description='Kozie', price=2.59),
             Product(name="Ser", description='wiejski', price=3.59),
             Product(name="Chleb", description='0.5kg', price=4.59),
             Product(name="masło", description='osełka', price=5.59),
             Product(name="piernik", description='toruński', price=7.59),
             Order(description="opis 1"),Order(description="opis 2"),
             Order(description="opis 3"), Order(description="opis 4"),
             Client(name="Slawek", surname='Boguslawski'),Client(name="Piotr", surname='Jaworski'),
             Client(name="Jan", surname='Kowalski'), Client(name="Grażyna", surname='Somsiad'),
             ]
    try:
        connection = make_connection()
        cursor = connection.cursor()
        for item in items:
            add_item_to_db(cursor, item)
        cursor.close()
        connection.close()
    except OperationalError as oe:
        print(oe)
    except Exception as e:
        print(e)

