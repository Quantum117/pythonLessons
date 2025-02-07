import fitz  # PyMuPDF for PDF processing
import requests
from PIL import Image
import os
import csv
import pandas as pd

LOG_FILE = "book_uploads.csv"

def log_upload_status(filename, file_path, status):
    """Log the upload status of books in a CSV file"""
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Book Name", "File Path", "Status"])

        writer.writerow([filename, file_path, status])


def filter_send_files(csv_file):
    try:
        df = pd.read_csv(csv_file)
        # Ensure the 'Status' column exists
        if 'Status' not in df.columns:
            print("Error: 'Status' column is missing in the CSV file.")
            return None, None
        success_files = df[df['Status'] == 'Success']
        failed_files = df[df['Status'] == "Failed - Too large"]
        # Optional: print or return the two DataFrames for inspection
        print("Successful uploads:")
        print(success_files)
        print("\nFailed uploads:")
        print(failed_files)

        # Returning two DataFrames: one for successful files and one for failed files
        return success_files, failed_files

    except Exception as e:
        print(f"Error reading or processing the CSV file: {e}")
        return None, None

