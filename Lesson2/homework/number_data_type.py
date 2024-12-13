def round_to_two_decimal_places(num):
    """
    Rounds a float number to 2 decimal places.
    """
    return round(num, 2)

def find_largest_and_smallest():
    """
    Asks for three numbers and outputs the largest and smallest.
    """
    nums = [float(input(f"Enter number {i + 1}: ")) for i in range(3)]
    return max(nums), min(nums)

def kilometers_to_meters_and_centimeters(km):
    """
    Converts kilometers to meters and centimeters.
    """
    meters = km * 1000
    centimeters = meters * 100
    return meters, centimeters

def integer_division_and_remainder(a, b):
    """
    Performs integer division and calculates the remainder of two numbers.
    """
    if b == 0:
        return "Division by zero is undefined."
    quotient = a // b
    remainder = a % b
    return quotient, remainder

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius temperature to Fahrenheit.
    """
    return celsius * 9/5 + 32

def last_digit(num):
    """
    Returns the last digit of a given number.
    """
    return abs(num) % 10

def is_even(num):
    """
    Checks if a number is even.
    """
    return num % 2 == 0

# Example usage of methods:
if __name__ == "__main__":
    # Task 1
    print("Rounded to two decimal places:", round_to_two_decimal_places(3.14159))

    # Task 2
    largest, smallest = find_largest_and_smallest()
    print(f"Largest: {largest}, Smallest: {smallest}")

    # Task 3
    meters, centimeters = kilometers_to_meters_and_centimeters(5)
    print(f"Meters: {meters}, Centimeters: {centimeters}")

    # Task 4
    quotient, remainder = integer_division_and_remainder(10, 3)
    print(f"Quotient: {quotient}, Remainder: {remainder}")

    # Task 5
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(25))

    # Task 6
    print("Last digit:", last_digit(12345))

    # Task 7
    print("Is the number even?:", is_even(4))
