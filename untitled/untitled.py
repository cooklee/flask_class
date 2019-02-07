from flask import Flask
from psql_connection import make_connection
from models import Product
from flask import request
app = Flask(__name__)
connection = make_connection()

@app.route('/')
def hello_world():
    return "<a href='/products/'> lista produktów</a>"

@app.route('/products/')
def show_all_products():
    cursor = connection.cursor()
    Product.get_all_item(cursor)
    ret_str = '<table><thead><tr><th>id</th><th>name</th><th>description</th><th>price</th></tr></thead><tbody>'
    for row in cursor :
        ret_str += "<tr>"
        for col in row:
            ret_str += f"<td>{col}</td>"
        ret_str += f"<td><a href='/usun?id={row[0]}'>usun</a></td>"
        ret_str += '</tr>'
    ret_str += '</tbody></table>'
    return ret_str

@app.route('/usun/', methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    Product.delete_item_on_id(connection.cursor(), id)
    return f'usunołem element o id = {id}'


if __name__ == '__main__':
    app.run()
