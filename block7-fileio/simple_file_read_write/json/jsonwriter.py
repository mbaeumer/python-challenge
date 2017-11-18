#!/usr/bin/python
import json
from product import Product

def write_json_file(filename, products):
  with open(filename, 'w') as outfile:
    json.dump(products, outfile, indent=4)
