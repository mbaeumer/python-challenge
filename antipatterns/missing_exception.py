

def divide_by_zero_with_generic_exception(dividend):
    try:
        result = dividend / 0
    except Exception as e:
        print("Exception occurred!")

def divide_by_zero_with_exception(dividend):
    try:
        result = dividend / 0
    except ZeroDivisionError as e:
        print("Illegal operation: Division by zero")

if __name__ == '__main__':
    divide_by_zero_with_generic_exception(5)
    divide_by_zero_with_exception(5)

