import re

def is_valid_minute(minute_string):
    return bool(re.match(r"^[0-5][0-9]$", minute_string))

def is_valid_hour_12(hour_string):
    return bool(re.match(r"^0[1-9]|1[0-2]$", hour_string))

def is_valid_hour_24(hour_string):
    return bool(re.match(r"^0[1-9]|1[0-9]|2[0-3]$", hour_string))

def is_valid_time_12(time_string):
    return bool(re.search(r"^(0[1-9]|1[0-2]):([0-5][0-9])$", time_string))

if __name__ == '__main__':
    print("00 ->", is_valid_minute("00"))
    print("59 ->",is_valid_minute("59"))
    print("62 ->", is_valid_minute("62"))
    print("590 ->",is_valid_minute("590"))

    print("09 ->",is_valid_hour_12("09"))
    print("12 ->",is_valid_hour_12("12"))
    print("13 ->",is_valid_hour_12("13"))

    print("09 ->",is_valid_hour_24("09"))
    print("17 ->",is_valid_hour_24("17"))
    print("22 ->",is_valid_hour_24("22"))
    print("26 ->",is_valid_hour_24("26"))

    print("09:15 ->", is_valid_time_12("09:15"))
    print("0915 ->", is_valid_time_12("0915"))
    print("09:64 ->", is_valid_time_12("09:64"))
    print("26:13 ->", is_valid_time_12("26:13"))