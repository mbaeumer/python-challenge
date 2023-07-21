import datetime

def calculate_age(today, birth_date):
    birth_date_this_year = birth_date.replace(year = today.year)
    today_year = today.year
    birth_year = birth_date.year
    if today < birth_date_this_year:
        result = today_year - birth_year - 1
        return result
    else:
        result = today_year - birth_year
        return result

if __name__ == '__main__':
    birth_date = datetime.datetime.strptime("1981-07-09", "%Y-%m-%d")
    today = datetime.datetime.today()
    calculate_age(today, birth_date)