class DataBaseObject:

    def create_dictionary(self):
        return {'table_name': self.table_name, 'fields': {}}


    @classmethod
    def get_all_item(cls, cursor):
        cursor.execute(f"select * from {cls.table_name}")

    @classmethod
    def delete_item_on_id(cls, cursor, id):
        cursor.execute(f"delete from {cls.table_name} where id={id}")



class Product(DataBaseObject):
    table_name = 'Product'

    def __init__(self, name, description, price):
        self.id = None
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def generate_create_sql(cls):
        query = f"""DROP TABLE {cls.table_name};
                    CREATE TABLE {cls.table_name} (
                    id serial,
                    name text,
                    description text,
                    price decimal(5,2),
                    PRIMARY KEY(id));"""
        return query

    def create_dictionary(self):
        base_dictionary = super().create_dictionary()
        base_dictionary['fields'] = {'name': self.name, 'description': self.description, 'price': self.price}
        return base_dictionary


class Order(DataBaseObject):
    table_name = 'Order2'

    def __init__(self, description):
        self.id = None
        self.description = description

    @classmethod
    def generate_create_sql(cls):
        query = f"""DROP TABLE {cls.table_name};
                CREATE TABLE {cls.table_name} (
                id serial,
                description text,
                PRIMARY KEY(id));"""
        return query

    def create_dictionary(self):
        base_dictionary = super().create_dictionary()
        base_dictionary['fields'] = {'description': self.description}
        return base_dictionary


class Client(DataBaseObject):
    table_name = 'Client'

    def __init__(self, name, surname):
        self.id = None
        self.name = name
        self.surname = surname

    @classmethod
    def generate_create_sql(cls):
        query = f"""DROP TABLE {cls.table_name};
                CREATE TABLE {cls.table_name} (
                id serial,
                name varchar(50),
                surname varchar(50),
                PRIMARY KEY(id));"""
        return query

    def create_dictionary(self):
        base_dictionary = super().create_dictionary()
        base_dictionary['fields'] = {'name': self.name, 'surname': self.surname}
        return {'table_name': self.table_name, 'name': self.name,
                'surname': self.surname}
