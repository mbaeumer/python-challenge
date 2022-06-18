
def bad():
    print("Bad example")
    car_brands = ['Mazda','Volkswagen','Volvo','Aston Martin']

    for index in range(len(car_brands)):
        print(index, car_brands[index])

def good():
    print("Good example")
    car_brands = ['Mazda', 'Volkswagen', 'Volvo', 'Aston Martin']

    for index, name in enumerate(car_brands):
        print(index, name)

if __name__ == '__main__':
    bad()
    good()