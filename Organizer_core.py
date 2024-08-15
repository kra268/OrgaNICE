import glob
import os
import sys
import shutil

# Define the source directory where your files are located
source_dir = '/Users/keerthanrao/Downloads/'
source_dir = os.path.join(source_dir)

# Function to create a folder if it does not exist
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Get a list of all files in the source directory
all_files = glob.glob(os.path.join(source_dir, '*'))

# Extract file extensions and create a set to store unique file types
file_types = set(os.path.splitext(file)[1] for file in all_files)

# Iterate through each unique file type
for file_type in file_types:
    # Skip directories
    if file_type == '':
        # print(f'{file_type} is a folder')
        continue

    # Create a folder for the current file type in the destination directory
    folder_name = file_type.replace('.', '') + '_files'
    folder_path = os.path.join(source_dir, folder_name)
    create_folder(folder_path)

    # Move each file to the corresponding folder
    for file in all_files:
        if file.endswith(file_type):
            shutil.move(file, folder_path)
            print(f"Moved {file} to {folder_path}")

print("Files sorted successfully.")
