# Task 1: Check if username and password are not empty
def check_username_password(username, password):
    if username and password:
        print("Username and password are valid.")
    else:
        print("Username or password cannot be empty.")

# Task 2: Check if two numbers are equal
def check_if_equal(num1, num2):
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")

# Task 3: Check if a number is positive and even
def check_positive_even(number):
    if number > 0 and number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is either not positive or not even.")

# Task 4: Check if all three numbers are different
def check_all_different(num1, num2, num3):
    if num1 != num2 and num1 != num3 and num2 != num3:
        print("All numbers are different.")
    else:
        print("Some numbers are the same.")

# Task 5: Check if two strings have the same length
def check_same_length(str1, str2):
    if len(str1) == len(str2):
        print("The strings have the same length.")
    else:
        print("The strings do not have the same length.")

# Task 6: Check if a number is divisible by both 3 and 5
def check_divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        print("The number is divisible by both 3 and 5.")
    else:
        print("The number is not divisible by both 3 and 5.")

# Task 7: Check if the sum of two numbers is greater than 50.8
def check_sum_greater_than_50_8(num1, num2):
    if num1 + num2 > 50.8:
        print("The sum of the numbers is greater than 50.8.")
    else:
        print("The sum of the numbers is not greater than 50.8.")

# Task 8: Check if a number is between 10 and 20 (inclusive)
def check_between_10_and_20(number):
    if 10 <= number <= 20:
        print("The number is between 10 and 20.")
    else:
        print("The number is not between 10 and 20.")

# Example usage
check_username_password("user123", "password123")
check_if_equal(5, 5)
check_positive_even(6)
check_all_different(1, 2, 3)
check_same_length("hello", "world")
check_divisible_by_3_and_5(15)
check_sum_greater_than_50_8(30, 25)
check_between_10_and_20(15)
