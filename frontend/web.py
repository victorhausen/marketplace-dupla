from flask import Flask, render_template, request

import sys

from werkzeug.utils import redirect
sys.path.append('f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla')

from backend.controller import Controller

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

marketplace_controller = Controller("marketplace_database.txt")
product_controller = Controller("product_database.txt")

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

        redirect("/")

    return render_template('create_marketplace.html')

@app.route('/products')
def products():
    
    return render_template('create_product.html')


app.run(debug=True)