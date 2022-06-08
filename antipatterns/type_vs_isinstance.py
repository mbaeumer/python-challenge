
def use_type():
    variable = 5
    print("The variable is of type %s" % type(variable))

def use_isinstance():
    variable = 5
    isint = isinstance(variable, int)
    if isint:
        print("The variable is of type int")

if __name__ == '__main__':
    use_type()
    use_isinstance()