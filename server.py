"""
Server.py file. Instantiates the Flask App with all required configs
"""

from flask import Flask, url_for, render_template, request, redirect, flash, jsonify
from models.model import RequestFeatureModel
from db import db
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/britecore'
app.secret_key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='


db.init_app(app)


def create_app():
    """
    Return an instance of the Flask App. used to create the database tables using SQLAlchemy
    :return:
    """
    return app


@app.route('/', methods=['POST', 'GET'])
def index():
    all_features = RequestFeatureModel.return_all()
    return render_template('index.html', data = all_features)

@app.route('/add-feature', methods=['POST', 'GET'])
def add_feature():
    return render_template('add.html')

@app.route('/new_ticket', methods=['POST', 'GET'])
def new():
    """
    Render the Request New Feature Template. Allowed Methods: POST, GET
    :return:
    """
    return render_template('add.html')


@app.route('/add-new', methods=['POST', 'GET'])
def add_new():
    """
    Function to add a new feature request to the database. Calls the save() function of the FeatureModel class.
    Allowed Methods: POST, GET
    :return:
    """
    title = request.form.get('title')
    description = request.form.get('description')
    client = request.form.get('client')
    client_priority = request.form.get('client_priority')
    target_date = request.form.get('target_date')
    product_areas = request.form.get('product_areas')
    created_at  = str(datetime.now())

    feature_model = RequestFeatureModel(title, description, client, client_priority, target_date, product_areas, created_at)
    feature_model.save()

    flash('Feature Request Added Successfully', 'success')
    return redirect(url_for('add_feature'))


@app.route('/search', methods=['POST', 'GET'])
def search_helper():
    """
    Get the list of feature requests by Search Params. Allowed Methods: POST, GET
    :return:
    """
    if request.method == 'POST':
        request_search_query = request.form.get('query')
        query_split = request_search_query.split(':')
        search = query_split[0]
        keyword = query_split[1]

        if search == 'date':
            data = RequestFeatureModel.find_by_date(keyword)
        elif search == 'client':
            data = RequestFeatureModel.find_by_client(keyword)
        else:
            data = RequestFeatureModel.find_by_product(keyword)
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
