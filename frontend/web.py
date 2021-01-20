import sys 
sys.path.append('.')

from flask import Flask, render_template, request, redirect
from backend.controller.marketplace_controller import MarketplaceController
from backend.controller.seller_controller import SellerController
from backend.controller.product_controller import ProductController
from backend.controller.log_controller import LogController
from backend.controller.category_controller import CategoryController
from backend.models.product import Product
from backend.models.category import Category
from backend.models.marketplace import Marketplace
from backend.models.seller import Seller

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('base_template.html')


@app.route('/marketplaces/<action>', methods=['GET', 'POST'])
def cadastrar_marketplaces(action):
    mp = None
    if request.method == 'POST':
        if action == 'Create':
            mp = Marketplace(request.form['name_input'], request.form['description_input'])
            MarketplaceController().create(mp)
            return redirect("/")
        elif action == 'Update':
            mp = MarketplaceController().read_by_id(request.form['id_input'])
            mp.name = request.form['name_input']
            mp.description=request.form['description_input']
            MarketplaceController().update(mp)
            return redirect("/list_marketplaces")
    return render_template('create_marketplace.html', marketplace=mp, action="Create")


@app.route('/list_marketplaces')
def listar_marketplace():
    lista_marketplace = MarketplaceController().read_all()
    return render_template('list_marketplace.html', listar=lista_marketplace)


@app.route('/update_marketplace/<id>')
def atualizar_marketplace(id):
    mp = MarketplaceController().read_by_id(id)
    return render_template('/create_marketplace.html', marketplace=mp, action="Update")


@app.route('/delete_marketplace/<id>')
def deletar_marketplace(id):
    mp = MarketplaceController().read_by_id(id)
    MarketplaceController().delete(mp)
    return redirect('/list_marketplaces')


@app.route('/products/<action>', methods=['GET', 'POST'])
def cadastrar_produtos(action):
    pr = None
    if request.method == 'POST':
        if action == 'Create':
            pr = Product(request.form['name_input'], request.form['description_input'], request.form['price_input'])
            ProductController().create(pr)
            return redirect("/")
        elif action == 'Update':
            pr = ProductController().read_by_id(request.form['id_input'])
            pr.name = request.form['name_input']
            pr.description = request.form['description_input']
            pr.price = request.form['price_input']
            ProductController().update(pr)
            return redirect("/list_products")
    return render_template('create_product.html', produtos=pr, action='Create')


@app.route('/list_products')
def listar_produtos():
    lista_produtos = ProductController().read_all()
    return render_template('list_product.html', produtos=lista_produtos)


@app.route('/update_products/<id>')
def atualizar_produtos(id):
    pr = ProductController().read_by_id(id)
    return render_template('create_product.html', produtos=pr, action='Update')


@app.route('/delete_products/<id>')
def deletar_produtos(id):
    prod = ProductController().read_by_id(id)
    ProductController().delete(prod)
    return redirect('/list_products')


@app.route('/categories/<action>', methods=['GET', 'POST'])
def cadastrar_categorias(action):
    ca = None
    if request.method == 'POST':
        if action == 'Create':
            ca = Category(request.form['name'], request.form['description'])
            CategoryController().create(ca)
            return redirect("/")
        elif action == 'Update':
            ca = CategoryController().read_by_id(request.form['id_input'])
            ca.name = request.form['name']
            ca.description = request.form['description']
            CategoryController().update(ca)
            return redirect('/list_categories')
    return render_template('create_categories.html', categorias=ca, action='Create')


@app.route('/list_categories')
def listar_categories():
    lista_categorias = CategoryController().read_all()
    return render_template('list_categories.html', lista=lista_categorias)


@app.route('/update_categories/<id>')
def atualizar_categorias(id):
    ca = CategoryController().read_by_id(id)
    return render_template('create_categories.html', categorias=ca, action='Update')


@app.route('/delete_categories/<id>')
def deletar_categorias(id):
    ca = CategoryController().read_by_id(id)
    CategoryController().delete(ca)
    return redirect('/list_categories')


@app.route('/sellers/<action>', methods=['GET', 'POST'])
def cadastrar_sellers(action):
    sel = None
    if request.method == 'POST':
        if action == 'Create':
            data = Seller(request.form['name_input'], request.form['contact_input'], request.form['email_input'])
            SellerController().create(data)
            return redirect("/list_sellers")
        elif action == 'Update':
            sel = SellerController().read_by_id(request.form['id_input'])
            sel.name = request.form['name_input']
            sel.phone = request.form['contact_input']
            sel.email = request.form['email_input']
            SellerController().update(sel)
            return redirect("/list_sellers")
    return render_template('create_seller.html', seller=sel, action="Create")


@app.route('/list_sellers')
def listar_sellers():
    sellers_list = SellerController().read_all()
    return render_template('list_seller.html', sellers=sellers_list)


@app.route('/update_seller/<id>')
def atualizar_seller(id):
    seller = SellerController().read_by_id(id)
    return render_template('/create_seller.html', seller=seller, action="Update")


@app.route('/delete_seller/<id>')
def deletar_seller(id):
    sel = SellerController().read_by_id(id)
    SellerController().delete(sel)
    return redirect('/list_sellers')


@app.route('/list_log')
def lista_logs():
    log_list = LogController().read()
    return render_template('list_log.html', log=log_list)


app.run(debug=True)
