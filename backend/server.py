""" we can use flask or django """

from urllib import response
from flask import Flask , request , jsonify
import product_DAO
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts' , methods=['GET'])
def get_products():
    products = product_DAO.get_all_products(connection)
    response = jsonify(products)
    #response.header.add('Access-Control-Allow-Origin' , '*')
    return response


if __name__ == '__main__':
    print("Starting python flask server for Grocery Store Management System")
    app.run(port=5000) 

