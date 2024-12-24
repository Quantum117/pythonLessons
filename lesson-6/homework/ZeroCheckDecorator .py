# Task1
"""
   Write a decorator function called check that verifies that
   the denominator is not equal to 0 and apply it to the following function:
"""
def check(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError :
            print("Denominator cannot be zero.")
            return None  # Indicates the operation failed
    return wrapper
@check
def div(a, b):
   return a / b

print(div(1, 2))
print(div(2, 0))