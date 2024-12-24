import os
import re

# File name for input
FILE_NAME = "sample.txt"

# File name for result output
OUTPUT_FILE = "word_count_report.txt"

# Ensure the input file exists
def ensure_file_exists():
    if not os.path.exists(FILE_NAME):
        print("File does not exist! Creating a new file.")
        with open(FILE_NAME, 'w') :
            pass  # Creates an empty file if one does not exist


# Analyze the text and extract words
def analyze_text():
    with open(FILE_NAME, 'r') as file:
        records = file.readlines()

    words = []
    if records:
        for record in records:
            # Split by non-word characters and convert to lowercase
            words.extend(re.split(r'\W+', record.lower()))
        # Remove empty strings from the result
        words = list(filter(None, words))
    else:
        print("Input file is empty.")
    return words


# Count the frequency of each word
def frequency_counter():
    words = analyze_text()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency


# Display the most common 'n' words and save them to a file
def display_most_common_words():
    # Get 'n' as input from the user
    try:
        n = int(input("Enter the number of most common words to display: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Get word counts
    word_frequency = frequency_counter()

    # Sort the dictionary by values (word frequencies) in descending order
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)

    # Get the top 'n' words
    top_n_words = sorted_word_frequency[:n]

    # Display the results
    print(f"Total Words : {sum(word_frequency.values())}")
    print(f"Top {n} most common Words:\n")
    for word, count in top_n_words:
        print(f"{word} - {count} times")

    # Save the results to 'result.txt'
    with open(OUTPUT_FILE, 'w') as output_file:
        output_file.write("Word Count Report\n")
        output_file.write(f"Total Words : {sum(word_frequency.values())}\n")
        output_file.write(f"Top {n} Words:\n")
        for word, count in top_n_words:
            output_file.write(f"{word} - {count} \n")

    print(f"\nThe result has been saved to '{OUTPUT_FILE}'.")


# Main function to execute the program
def main():
    ensure_file_exists()
    display_most_common_words()


# Call the main function
if __name__ == "__main__":
    main()
