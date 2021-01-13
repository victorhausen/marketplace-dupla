from flask import Flask, render_template, request
from werkzeug.utils import redirect
from backend.controller.marketplace_controller import creating_marketplace, reading_marketplaces
from backend.controller.product_controller import creating_product, reading_products
from backend.controller.seller_controller import reading_sellers, creating_seller
from backend.controller.log_controller import reading_log
from backend.controller.category_controller import reading_categories, creating_category
from backend.models.product import Product
from backend.models.category import Category
from backend.models.marketplace import Marketplace
from backend.models.seller import Seller

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('base_template.html')


@app.route('/marketplaces', methods=['GET', 'POST'])
def cadastrar_marketplaces():
    if request.method == 'POST':
        mp = Marketplace(request.form['name_input'], request.form['description_input'])
        creating_marketplace(mp)
        redirect("/")
    return render_template('create_marketplace.html')


@app.route('/list_marketplaces')
def listar_marketplace():
    lista_marketplace = reading_marketplaces()
    return render_template('list_marketplace.html', listar=lista_marketplace)


@app.route('/products', methods=['GET', 'POST'])
def cadastrar_produtos():
    if request.method == 'POST':
        pr = Product(request.form['name_input'], request.form['description_input'], request.form['price_input'])
        creating_product(pr)
        redirect("/")
    return render_template('create_product.html')


@app.route('/list_products')
def listar_produtos():
    lista_produtos = reading_products()
    return render_template('list_product.html', produtos=lista_produtos)


@app.route('/categories', methods=['GET', 'POST'])
def cadastrar_categorias():
    if request.method == 'POST':
        ca = Category(request.form['name'], request.form['description'])
        creating_category(ca)
        redirect("/")
    return render_template('create_categories.html')


@app.route('/list_categories')
def listar_categories():
    lista_categorias = reading_categories()
    return render_template('list_categories.html', lista=lista_categorias)


@app.route('/sellers', methods=['GET', 'POST'])
def cadastrar_sellers():
    if request.method == 'POST':
        data = Seller(request.form['full_name'], request.form['contact_number'], request.form['seller_email'])
        creating_seller(data)
        redirect("/")
    return render_template('create_seller.html')


@app.route('/list_sellers')
def listar_sellers():
    sellers_list = reading_sellers()
    return render_template('list_seller.html', sellers=sellers_list)


@app.route('/list_log')
def lista_logs():
    log_list = reading_log()
    return render_template('list_log.html', log=log_list)


app.run(debug=True)
