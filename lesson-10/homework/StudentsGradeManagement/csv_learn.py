import csv
from collections import defaultdict
import os

# Step 1: Read data from grades.csv and store it in a list of dictionaries
def read_grades(filename):
    try:
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                grades = [row for row in reader]
            return grades
        else: print("file does not exist")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

# Step 2: Calculate the average grade for each subject
def calculate_average_grades(grades):
    try:
        subject_grades = defaultdict(list)

        # Group grades by subject
        for entry in grades:
            try:
                subject = entry['Subject']
                grade = float(entry['Grade'])
                subject_grades[subject].append(grade)
            except ValueError:
                print(f"Invalid grade value encountered: {entry['Grade']}")

        # Calculate averages
        average_grades = {
            subject: sum(grades) / len(grades) if grades else 0
            for subject, grades in subject_grades.items()
        }
        return average_grades
    except Exception as e:
        print(f"An error occurred while calculating averages: {e}")
        return {}

# Step 3: Write the average grades to average_grades.csv
def write_average_grades(filename, average_grades):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Subject', 'Average Grade'])
            for subject, average in average_grades.items():
                writer.writerow([subject, round(average, 2)])
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

# Main program
def main():
    input_file = 'grades.csv'
    output_file = 'average_grades.csv'

    # Read grades
    grades = read_grades(input_file)

    if not grades:
        print("No data to process. Exiting.")
        return

    # Calculate averages
    average_grades = calculate_average_grades(grades)

    # Write averages to a new CSV file
    write_average_grades(output_file, average_grades)
    print(f"Average grades have been written to {output_file}.")

if __name__ == "__main__":
    main()
