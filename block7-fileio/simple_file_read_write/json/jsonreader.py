#!/usr/bin/python
import json
from product import Product

def read_json_file(filename):
  products = []
  try:
    with open(filename) as data_file:
      data = json.load(data_file)
    products_json = data["products"]
    for p in products_json:
      product = Product(p['name'], p['price'], p['quantity'])
      products.append(product)
  except FileNotFoundError:
    raise FileNotFoundError
  return products

def read_raw_data(filename):
  data = {}
  try:
    with open(filename) as data_file:    
      data = json.load(data_file)
  except FileNotFoundError:
    raise FileNotFoundError
  return data 
