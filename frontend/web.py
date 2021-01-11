import sys
sys.path.append('backend/controller')

from flask import Flask, render_template, request
from werkzeug.utils import redirect
from log import write_log
from marketplace import create_marketplace, get_marketplaces
from product import create_product, get_product
from log import write_log, get_log

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

@app.route('/sellers')
def sellers():
    if request.args:
        data = {
            'full_name': request.args['full_name'],
            'contact': request.args['contact_number'],
            'email': request.args['seller_email']
        }
        seller_controller.create(data)
        write_log(action='register', type='seller')
    write_log(action="list",type="products")
    return render_template('register_seller.html', produtos = lista_produtos)

@app.route('/list_sellers')
def list_sellers():
    sellers_list = seller_controller.get_seller()
    write_log(action="list",type="sellers")
    return render_template('list_seller.html', sellers = sellers_list)

@app.route('/list_log')
def lista_log():
    log_list = log_controller.get_log()
    write_log(action="list",type="log")
    return render_template('list_log.html', log = log_list)

app.run(debug=True)