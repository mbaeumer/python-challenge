
def group_items(list):
    item_count = {}

    for item in list:
        if item in item_count:
            item_value = item_count[item]
            item_value = item_value + 1
            item_count[item] = item_value
        else:
            item_count[item] = 1

    return item_count

if __name__ == '__main__':
    list = ['A', 'B', 'C', 'B', 'B', 'C', 'B', 'A']
