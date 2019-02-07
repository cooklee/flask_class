from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import connection_info as ci


def make_connection(isolation_level=ISOLATION_LEVEL_AUTOCOMMIT):
    connection = connect(user=ci['username'],
                         password=ci['password'],
                         host=ci['host'],
                         database=ci['database'],
                         port=ci['port'])
    connection.set_isolation_level(isolation_level)
    return connection
