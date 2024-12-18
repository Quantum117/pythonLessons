import random

# Task1

def uncommon_elements(list1, list2):
    """ Return Uncommon Elements of Lists"""

    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    uncommon = list((c1 - c2).elements()) + list((c2 - c1).elements())
    return uncommon

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # Output: [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # Output: [2, 2, 5]

#Task2
def print_squares(n):
    for i in range(1, n):
        print(i ** 2)
print_squares(5)
# Output:
# 1
# 4
# 9
# 16

#Task3
def modify_string(txt):
    """ 3. Insert Underscores After Conditions """

    vowels = "aeiou"
    result = []
    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1) % 3 == 0 or char in vowels:
            if i != len(txt) - 1:
                result.append('_')
    return ''.join(result)

print(modify_string("hello"))  # Output: hel_lo
print(modify_string("assalom"))  # Output: ass_alom
print(modify_string("abcabcdabcdeabcdefabcdefg"))  # Output: abc_abcd_abcdeab_cdef_abcdefg

#Task4
def number_guessing_game():
    """4. Number Guessing Game"""
    while True:
        number = random.randint(1, 100)
        attempts = 10
        print("Guess the number between 1 and 100.")
        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
                if guess > number:
                    print("Too high!")
                elif guess < number:
                    print("Too low!")
                else:
                    print("You guessed it right!")
                    return
                attempts -= 1
            except ValueError:
                print("Please enter a valid number.")
        print("You lost. Want to play again?")
        response = input("Enter 'Y' to play again: ").lower()
        if response not in ['y', 'yes', 'ok']:
            break

number_guessing_game()

#Task5
def password_checker():
    """Password Checker"""
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

password_checker()

#Task6
def print_primes():
    """Print Primes"""
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

print_primes()
# Output: List of all prime numbers between 1 and 100
