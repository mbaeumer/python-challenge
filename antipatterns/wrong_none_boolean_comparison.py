

def bad():
    iscorrect = True
    print(iscorrect==None)
    print(iscorrect==True)

def good():
    iscorrect = True
    print(iscorrect is None)
    print(iscorrect is True)

if __name__ == '__main__':
    bad()
    good()
