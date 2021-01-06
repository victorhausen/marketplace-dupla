from flask import Flask, render_template, request

import sys

from werkzeug.utils import redirect
#sys.path.append('f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla')
#sys.path.append('/home/victor/Documents/marketplace-dupla')
#sys.path.append('/home/quesia/marketplace-dupla')
sys.path.append('.')

from backend.controller import Controller
from backend.log import write_log

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

marketplace_controller = Controller("database/marketplace_database.txt")
product_controller = Controller("database/product_database.txt")
categories_controller = Controller("database/categories_database.txt")
lista_produtos = product_controller.get_product()
lista_categories = categories_controller.get_categories()


@app.route('/')
def index():
    return render_template('base_template.html')


@app.route('/marketplaces')
def marketplaces():
    if request.args:
        data = {
            "name": request.args["name"],
            "description": request.args["description"]
        }
        marketplace_controller.create(data)
        write_log(action="create",type="marketplace")
        redirect("/")

    return render_template('create_marketplace.html')

@app.route('/products')
def products():
    if request.args:
        data = {
            "name": request.args["name"],
            "description": request.args["description"],
            "price":request.args["price"]
        }
        product_controller.create(data)
        write_log(action="create",type="product")
        
        redirect("/")

    return render_template('create_product.html')

@app.route('/lista_marketplaces')
def listar_marketplace():
    lista_marketplace = marketplace_controller.get_marketplace()
    write_log(action='read', type='marketplace')
    return render_template('list_marketplace.html', listar = lista_marketplace)

@app.route('/list_products')
def listar_produtos():
    lista_produtos = product_controller.get_product()
    write_log(action="list",type="products")
    return render_template('list_product.html', produtos = lista_produtos)

@app.route('/categories')
def cadastrar_categorias():
    if request.args:
        data = {
            "name": request.args["name"],
            "description": request.args["description"]
        }
        categories_controller.create(data)
        write_log(action="create", type="category")
        redirect("/")
    return render_template('create_categories.html')

@app.route('/list_categories')
def listar_categories():
    lista_categorias = categories_controller.get_categories()
    write_log(action="list", type="categories")
    return render_template('list_categories.html', lista = lista_categorias)


app.run(debug=True)