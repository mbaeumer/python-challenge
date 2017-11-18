#!/usr/bin/python

class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def to_dict(self):
    data = {}
    data['name'] = self.name
    data['price'] = self.price
    data['quantity'] = self.quantity
    return data
