from flask import Flask, request
from handlepaypalrequest import GetOrder


app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/paypal-transaction-complete', methods=['POST'])
def handle_paypal_request():
    return GetOrder().get_order(request.json['orderID'])
