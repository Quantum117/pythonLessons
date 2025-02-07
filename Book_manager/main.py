import os
import fitz  # PyMuPDF for PDF processing
import requests
from PIL import Image
import os
import json
from helper_methods import log_upload_status, filter_send_files, LOG_FILE

# Telegram Bot Details
bot_token = "7670945462:AAEAf7GuQtJ7tuAlWZ5K45DgMGEjs_XcNIc"
CHANNEL_ID = "-1002338200529"  # Replace with your channel name or ID

# Directory where books are stored
BOOKS_DIR = r"C:\Users\user\Downloads\Telegram Desktop\Books"  # Use raw string literal
MAX_FILE_SIZE_MB = 30

# Check if the directory exists
if not os.path.exists(BOOKS_DIR):
    print(f"Error: The directory '{BOOKS_DIR}' does not exist!")
else:
    print(f"Directory '{BOOKS_DIR}' exists. Proceeding with the process...")

# Function to send an image
def send_photo(image_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    with open(image_path, "rb") as img:
        files = {"photo": img}
        data = {"chat_id": CHANNEL_ID}
        response = requests.post(url, data=data, files=files)
        #print(response.json())
        return response.json().get('result').get('message_id')

# Function to extract and save first page of a PDF as an image
def extract_first_page_as_image(pdf_path):
    doc = fitz.open(pdf_path)  # Open PDF
    first_page = doc.load_page(0)  # Get the first page
    pix = first_page.get_pixmap()  # Render page as image
    img_path = pdf_path.replace(".pdf", "_first_page.jpg")
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Convert to image
    img.save(img_path, "JPEG")  # Save as JPEG
    return img_path

# Process each file in directory
def process_books(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # If it's a PDF
        if filename.endswith(".pdf"):
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB

            if file_size_mb > MAX_FILE_SIZE_MB:
                print(f"Skipping {filename}: File size exceeds 50MB")
                log_upload_status(filename, file_path, "Failed - Too large")
                continue
            image_path = extract_first_page_as_image(file_path)  #Extract first page as image
            message_id = send_photo(image_path) # Send the image
            with open(file_path, 'rb') as file :
                url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
                response = requests.post(url, data={"chat_id": CHANNEL_ID, "reply_to_message_id": message_id }, files={"document": file} )
                # print(response)
                success = response.json().get("ok", False)
                log_upload_status(filename, file_path, "Success" if success else "Failed")

# Run the function
process_books(BOOKS_DIR)
filter_send_files(LOG_FILE)