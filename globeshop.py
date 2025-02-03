# globalshop.py
from flask import Flask, request, jsonify
import pandas as pd
user_behavior = pd.read_csv('user_behavior.csv')
purchase_history = pd.read_csv('purchase_history.csv')
app = Flask(__name__)

@app.route('/')
def index():
    return 'GlobeShop Recommendation System'

if __name__ == '__main__':
    app.run(debug=True, port=5001)