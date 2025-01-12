import os

# Get the directory of the current script
current_file_directory = os.path.dirname(os.path.abspath(__file__))

print("Current file is in:", current_file_directory)
dir(current_file_directory)
