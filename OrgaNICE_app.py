import glob
import os
import shutil
import tkinter as tk
from tkinter import filedialog
import sys
import threading


# Function to create a folder if it does not exist
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Function to select a directory
def browse_directory():
    global source_dir
    source_dir = filedialog.askdirectory(title="Select Directory")
    if source_dir:
        selected_dir_label.config(text=f"Selected Directory: {source_dir}")
        message_label.config(text="")  # Clear any previous messages


# Function to sort files in the selected directory
def sort_files():
    if not source_dir:
        message_label.config(text="Please select a directory first.", fg="red")
        return

    # Get a list of all files in the source directory
    all_files = glob.glob(os.path.join(source_dir, '*'))

    # Extract file extensions and create a set to store unique file types
    file_types = set(os.path.splitext(file)[1] for file in all_files)

    # Iterate through each unique file type
    for file_type in file_types:
        # Skip directories
        if file_type == '':
            continue

        # Create a folder for the current file type in the source directory
        folder_name = file_type.replace('.', '') + '_files'
        folder_path = os.path.join(source_dir, folder_name)
        create_folder(folder_path)

        # Move each file to the corresponding folder
        for file in all_files:
            if file.endswith(file_type):
                shutil.move(file, folder_path)
                output_text.insert(tk.END, f"Moved {file} to {folder_path}\n")
                output_text.see(tk.END)  # Scroll to the end of the text box

    message_label.config(text="Files sorted successfully!", fg="green")


# Function to create the GUI
def create_gui():
    global selected_dir_label, message_label, output_text

    root = tk.Tk()
    root.title("File Sorter")

    # Set the window size (width x height)
    root.geometry("500x400")

    # Create and place a button for browsing directories
    browse_button = tk.Button(root, text="Browse Directory", command=browse_directory)
    browse_button.pack(pady=10)

    # Label to show the selected directory
    selected_dir_label = tk.Label(root, text="No directory selected")
    selected_dir_label.pack(pady=5)

    # Create and place a button for sorting files
    sort_button = tk.Button(root, text="Sort Files", command=lambda: threading.Thread(target=sort_files).start())
    sort_button.pack(pady=10)

    # Label to display messages
    message_label = tk.Label(root, text="")
    message_label.pack(pady=5)

    # Text widget to display the terminal output
    output_text = tk.Text(root, height=15, width=60)
    output_text.pack(pady=10)

    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    source_dir = None  # Initialize the source directory variable
    create_gui()
