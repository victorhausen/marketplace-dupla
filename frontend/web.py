from flask import Flask, render_template, request
from werkzeug.utils import redirect
from backend.controller.marketplace_controller import creating_marketplace, reading_marketplaces
from backend.controller.product_controller import creating_product, reading_products, updating_products, deleting_product, reading_product_by_id
from backend.controller.seller_controller import reading_sellers, creating_seller
from backend.controller.log_controller import reading_log
from backend.controller.category_controller import reading_categories, creating_category, updating_categories, deleting_categories, reading_categories_by_id
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


@app.route('/products/<action>', methods=['GET', 'POST'])
def cadastrar_produtos(action):
    pr = None
    if request.method == 'POST':
        if action == 'Create':
            pr = Product(request.form['name_input'], request.form['description_input'], request.form['price_input'])
            creating_product(pr)
            return redirect("/")
        elif action == 'Update':
            pr = Product(request.form['name_input'], request.form['description_input'], request.form['price_input'], request.form['id_input'])
            updating_products(pr)
            return redirect("/list_products")
    return render_template('create_product.html', produtos=pr, action='Create')


@app.route('/list_products')
def listar_produtos():
    lista_produtos = reading_products()
    return render_template('list_product.html', produtos=lista_produtos)


@app.route('/update_products/<id>')
def atualizar_produtos(id):
    pr = reading_product_by_id(id)
    return render_template('create_product.html', produtos=pr, action='Update')


@app.route('/delete_products/<id>')
def deletar_produtos(id):
    deleting_product(id)
    return redirect('/list_products')


@app.route('/categories/<action>', methods=['GET', 'POST'])
def cadastrar_categorias(action):
    ca = None
    if request.method == 'POST':
        if action == 'Create':
            ca = Category(request.form['name'], request.form['description'])
            creating_category(ca)
            return redirect("/")
        elif action == 'Update':
            ca = Category(request.form['name'], request.form['description'], request.form['id_input'])
            updating_categories(ca)
            return redirect('/list_categories.html')
    return render_template('create_categories.html', categorias=ca, action='Create')


@app.route('/list_categories')
def listar_categories():
    lista_categorias = reading_categories()
    return render_template('list_categories.html', lista=lista_categorias)


@app.route('/update_categories/<id>')
def atualizar_categorias(id):
    ca = reading_categories_by_id(id)
    return render_template('create_categories.html', categorias=ca, action='Update')


@app.route('/delete_categories/<id>')
def deletar_categorias(id):
    deleting_categories(id)
    return redirect('/list_categories')


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
