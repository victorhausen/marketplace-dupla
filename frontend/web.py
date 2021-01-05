from flask import Flask, render_template, request

import sys

from werkzeug.utils import redirect
#sys.path.append('f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla')
sys.path.append('/home/victor/Documents/marketplace-dupla')

from backend.controller import Controller
from backend.log import write_log

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

marketplace_controller = Controller("./database/marketplace_database.txt")
product_controller = Controller("./database/product_database.txt")

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


app.run(debug=True)