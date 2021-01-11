import sys
sys.path.append('.')

from flask import Flask, render_template, request
from werkzeug.utils import redirect
from backend.controller.marketplace_controller import creating_marketplace, list_marketplaces
from backend.controller.product_controller import creating_product, list_products
from backend.controller.log_controller import write_log, get_log
from backend.controller.seller_controller import list_sellers, creating_seller
from backend.controller.category_controller import list_categories, creating_category

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('base_template.html')

@app.route('/marketplaces', methods=['GET', 'POST'])
def marketplaces():
    if request.method == 'POST':
        name = request.form['name_input']
        description = request.form['description_input']
        creating_marketplace(name, description)
        write_log(action="create",type="marketplace")
        redirect("/")
    return render_template('create_marketplace.html')

@app.route('/list_marketplaces')
def listar_marketplace():
    lista_marketplace = list_marketplaces()
    write_log(action='list', type='marketplace')
    return render_template('list_marketplace.html', listar = lista_marketplace)

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        name = request.form['name_input']
        description = request.form['description_input']
        price = request.form['price_input']
        creating_product(name, description, price)
        write_log(action="create",type="product")
        redirect("/")
    return render_template('create_product.html')

@app.route('/list_products')
def listar_produtos():
    lista_produtos = list_products()
    write_log(action="list",type="products")
    return render_template('list_product.html', produtos = lista_produtos)

@app.route('/categories', methods=['GET', 'POST'])
def cadastrar_categorias():
    if request.method == 'POST':
        data = request.form
        creating_category(data)
        write_log(action="create", type="category")
        redirect("/")
    return render_template('create_categories.html')

@app.route('/list_categories')
def listar_categories():
    lista_categorias = list_categories()
    write_log(action="list", type="categories")
    return render_template('list_categories.html', lista = lista_categorias)

@app.route('/sellers', methods=['GET', 'POST'])
def sellers():
    if request.method == 'POST':
        data = request.form
        creating_seller(data)
        write_log(action='register', type='seller')
    return render_template('create_seller.html')

@app.route('/list_sellers')
def list_seller():
    sellers_list = list_sellers()
    write_log(action="list",type="sellers")
    return render_template('list_seller.html', sellers = sellers_list)

@app.route('/list_log')
def lista_log():
    log_list = get_log()
    write_log(action="list",type="log")
    return render_template('list_log.html', log = log_list)

app.run(debug=True)