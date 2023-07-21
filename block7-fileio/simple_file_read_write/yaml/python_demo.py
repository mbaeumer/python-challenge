#!/usr/bin/python
import yaml

def read_yaml_file():
    with open(r'data.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)

    print(fruits_list)

if __name__ == '__main__':
    read_yaml_file()
