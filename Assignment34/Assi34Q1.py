# Logging System
# Create a Logs/folder
# Store:
# Backup start time
# Files copied
# Zip file name
# Errors(if any)

import os
import sys
import zipfile
import logging
import smtplib
from datetime import datetime
from email.message import EmailMessage

# ---------------- CONFIGURATION ----------------

LOG_FOLDER = "Logs"
HISTORY_FILE = "backup_history.txt"
EXCLUDE_EXTENSIONS = ['.tmp', '.log', '.exe']

# ---------------- LOGGING SYSTEM ----------------

def setup_logging():
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)

    log_filename = os.path.join(
        LOG_FOLDER,
        f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Backup process started")
    return log_filename

# ---------------- BACKUP FUNCTION ----------------

def create_backup(source_folder):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"Backup_{timestamp}.zip"

        file_count = 0

        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(source_folder):
                for file in filenames:
                    if not any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                        filepath = os.path.join(foldername, file)
                        zipf.write(filepath,
                                   os.path.relpath(filepath, source_folder))
                        file_count += 1

        zip_size = os.path.getsize(zip_filename)

        logging.info(f"Files copied: {file_count}")
        logging.info(f"Zip file name: {zip_filename}")
        logging.info(f"Zip size: {zip_size} bytes")

        update_history(zip_filename, file_count, zip_size)

        return zip_filename

    except Exception as e:
        logging.error(f"Error: {str(e)}")

# ---------------- RESTORE FUNCTION ----------------

def restore_backup(zip_file, destination):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(destination)

        logging.info(f"Backup restored to {destination}")
        print("Restore completed successfully")

    except Exception as e:
        logging.error(f"Restore error: {str(e)}")

# ---------------- EMAIL FUNCTION ----------------

def send_email(log_file, zip_file):
    try:
        sender = "your_email@gmail.com"
        receiver = "receiver_email@gmail.com"
        password = "your_app_password"

        msg = EmailMessage()
        msg['Subject'] = "Backup Completed Successfully"
        msg['From'] = sender
        msg['To'] = receiver
        msg.set_content("Backup completed successfully. Please find log attached.")

        # Attach log file
        with open(log_file, 'rb') as f:
            msg.add_attachment(f.read(),
                               maintype='application',
                               subtype='octet-stream',
                               filename=os.path.basename(log_file))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

        logging.info("Email sent successfully")

    except Exception as e:
        logging.error(f"Email error: {str(e)}")

# ---------------- HISTORY FUNCTION ----------------

def update_history(zip_name, file_count, zip_size):
    with open(HISTORY_FILE, 'a') as f:
        f.write(f"{datetime.now()} | {zip_name} | Files: {file_count} | Size: {zip_size} bytes\n")

def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            print(f.read())
    else:
        print("No backup history available")

# ---------------- MAIN FUNCTION ----------------

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("Backup: python Script.py FolderPath")
        print("Restore: python Script.py --restore ZipFile Destination")
        print("History: python Script.py --history")
        return

    log_file = setup_logging()

    if sys.argv[1] == "--restore":
        restore_backup(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "--history":
        show_history()

    else:
        source_folder = sys.argv[1]

        if not os.path.exists(source_folder):
            print("Invalid folder path")
            return

        zip_file = create_backup(source_folder)
        send_email(log_file, zip_file)

# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment\Assignment34>python Assi34Q1.py
# Usage:
# Backup: python Script.py FolderPath
# Restore: python Script.py --restore ZipFile Destination
# History: python Script.py --history    