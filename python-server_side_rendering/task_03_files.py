#!/usr/bin/env python3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    with open('products.json') as f:
        return json.load(f)


def read_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items=data['items'])


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        data = [p for p in data if str(p['id']) == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
