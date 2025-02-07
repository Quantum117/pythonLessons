import os

directory_path =  r"C:\Users\user\Downloads\Telegram Desktop\Books"

if os.path.exists(directory_path):
    print("The directory exists.")
else:
    print("The directory does not exist.")
