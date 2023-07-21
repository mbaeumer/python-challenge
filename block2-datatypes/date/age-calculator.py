import datetime

def calculate_age(today, birth_date):
    print("age: ", (today - birth_date).days // 365)
    print("modulo: ", (today - birth_date).days % 365)

if __name__ == '__main__':
    birth_date = datetime.datetime.strptime("1981-07-09", "%Y-%m-%d")
    today = datetime.datetime.today()
    calculate_age(today, birth_date)