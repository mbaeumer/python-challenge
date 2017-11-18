#!/usr/bin/python
from product import Product
from jsonwriter import write_json_file
from jsonreader import read_json_file
from jsonreader import read_raw_data

def main():
  print_title()
  print("STEP 1: Reading the raw data only")
  raw_data = handle_raw_data()
  print(raw_data)

  products = handle_serialized_data()
  print("STEP 2: Reading the raw data and create Product objects")
  for p in products:
    print("Name: %s, price: %f, quantity: %d" % (p.name, p.price, p.quantity))

  products.append(create_dummy_product())

  print("STEP 3: Writing the data to the file")
  write_json_file("products.json", prepare_data_to_write(products))

def print_title():
  print("Demo of handling json files\n")

def handle_raw_data():
  data = {} 
  try:
    data = read_raw_data("products.json")
  except FileNotFoundError:
    print("ERROR: The file does not exist!")
    raise FileNotFoundError
  return data

def handle_serialized_data():
  products = []
  try:
    products = read_json_file("products.json")
  except FileNotFoundError:
    print("ERROR: The file does not exist!")
    raise FileNotFoundError
  return products

def create_dummy_product():
  return Product("new-product", 1234, 4321)

def prepare_data_to_write(products):
  products_dictionaries = []
  for p in products:
    products_dictionaries.append(p.to_dict())
  data = {"products": products_dictionaries}
  return data

if __name__ == '__main__':
  main()
