def get_name_and_age():
    """
    Asks for the user's name and year of birth, then calculates their age.
    """
    name = input("Enter your name: ")
    year_of_birth = int(input("Enter your year of birth: "))
    age = 2024 - year_of_birth
    return name, age

def extract_car_names(txt):
    """
    Extracts car names from a given scrambled text.
    """
    return ''.join(filter(str.isupper, txt))

def string_operations():
    """
    Takes a string input, prints length, and converts to uppercase and lowercase.
    """
    user_string = input("Enter a string: ")
    length = len(user_string)
    upper = user_string.upper()
    lower = user_string.lower()
    return length, upper, lower

def is_palindrome(string):
    """
    Checks if a string is a palindrome.
    """
    return string == string[::-1]

def count_vowels_and_consonants(string):
    """
    Counts the number of vowels and consonants in a string.
    """
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in string if char in vowels)
    consonant_count = sum(1 for char in string if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

def string_contains(substring, string):
    """
    Checks if one string contains another.
    """
    return substring in string

def replace_word(sentence, old_word, new_word):
    """
    Replaces a word in a sentence with another word.
    """
    return sentence.replace(old_word, new_word)

def first_and_last_characters(string):
    """
    Prints the first and last characters of a string.
    """
    return string[0], string[-1]

def reverse_string(string):
    """
    Reverses a given string.
    """
    return string[::-1]

def word_count(sentence):
    """
    Counts the number of words in a sentence.
    """
    return len(sentence.split())

def contains_digits(string):
    """
    Checks if a string contains any digits.
    """
    return any(char.isdigit() for char in string)

def join_words(words, separator):
    """
    Joins a list of words into a single string separated by a character.
    """
    return separator.join(words)

def remove_spaces(string):
    """
    Removes all spaces from a string.
    """
    return string.replace(' ', '')

def check_strings_equality(string1, string2):
    """
    Checks if two strings are equal.
    """
    return string1 == string2

def create_acronym(sentence):
    """
    Creates an acronym from the first letters of each word in a sentence.
    """
    return ''.join(word[0].upper() for word in sentence.split())

def remove_character(string, char):
    """
    Removes all occurrences of a character from a string.
    """
    return string.replace(char, '')

def replace_vowels(string, symbol):
    """
    Replaces all vowels in a string with a given symbol.
    """
    vowels = 'aeiouAEIOU'
    return ''.join(symbol if char in vowels else char for char in string)

def starts_and_ends_with(string, start_word, end_word):
    """
    Checks if a string starts with one word and ends with another.
    """
    return string.startswith(start_word) and string.endswith(end_word)

# Example usage of methods:
if __name__ == "__main__":
    # Task 1
    name, age = get_name_and_age()
    print(f"Name: {name}, Age: {age}")

    # Task 2
    txt = 'LMaasleitbtui'
    print("Extracted car names:", extract_car_names(txt))

    # Task 3
    length, upper, lower = string_operations()
    print(f"Length: {length}, Upper: {upper}, Lower: {lower}")

    # Task 4
    print("Is palindrome:", is_palindrome("madam"))

    # Task 5
    vowels, consonants = count_vowels_and_consonants("Hello World")
    print(f"Vowels: {vowels}, Consonants: {consonants}")

    # Task 6
    print("Contains substring:", string_contains("love", "I love apples."))

    # Task 7
    print("Replaced sentence:", replace_word("I love apples.", "apples", "oranges"))

    # Task 8
    print("First and last characters:", first_and_last_characters("Python"))

    # Task 9
    print("Reversed string:", reverse_string("Python"))

    # Task 10
    print("Number of words:", word_count("I love Python programming"))

    # Task 11
    print("Contains digits:", contains_digits("Python3"))

    # Task 12
    print("Joined words:", join_words(["Python", "is", "fun"], "-"))

    # Task 13
    print("String without spaces:", remove_spaces("Python is fun"))

    # Task 14
    print("Strings are equal:", check_strings_equality("hello", "hello"))

    # Task 15
    print("Acronym:", create_acronym("World Health Organization"))

    # Task 16
    print("String without character:", remove_character("hello world", "o"))

    # Task 17
    print("String with replaced vowels:", replace_vowels("hello", "*"))

    # Task 18
    print("Starts and ends with:", starts_and_ends_with("Python is fun!", "Python", "fun!"))
