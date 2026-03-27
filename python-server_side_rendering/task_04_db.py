#!/usr/bin/env python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


def read_json():
    with open('products.json') as f:
        return json.load(f)


def read_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_sql(product_id=None):
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row       # lignes accessibles comme des dicts
    cursor = conn.cursor()

    if product_id:
        cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
    else:
        cursor.execute('SELECT * FROM Products')

    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]   # convertit en liste de dicts


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql(product_id)
        if product_id and not data:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=data)
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrage par id pour json et csv
    if product_id:
        data = [p for p in data if str(p['id']) == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
