
def init_list():
    names=[]
    names.append("Joe")
    names.append("Lotta")
    names.append("Pelle")
    names.append("Kalle")

    return names

def list_to_dict(names):
    return dict(enumerate(names))

def print_dict(dict):
    for k,v in dict.items():
        print(str(k) + "-" + v)

if __name__ == '__main__':
    names = init_list()
    dict_names = list_to_dict(names)
    print_dict(dict_names)