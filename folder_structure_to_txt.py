import os
import subprocess
import argparse
import tkinter as tk
from tkinter import filedialog
import sys
import datetime

def select_folder_dialog():
    """Open a dialog to select a folder"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select folder to analyze")
    root.destroy()
    return folder_path

def select_output_file_dialog(default_filename="directory_tree.txt"):
    """Open a dialog to select where to save the output file"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(
        title="Save folder structure as",
        defaultextension=".txt",
        initialfile=default_filename,
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    root.destroy()
    return file_path

# Function to list the directory tree with tree-like formatting
def list_directory_tree(target_dir, prefix=""):
    lines = []
    try:
        items = sorted(os.listdir(target_dir))
        for index, item in enumerate(items):
            item_path = os.path.join(target_dir, item)
            is_last = (index == len(items) - 1)
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{item}")
            if os.path.isdir(item_path):
                extension = "    " if is_last else "│   "
                lines.extend(list_directory_tree(item_path, prefix + extension))
    except PermissionError:
        lines.append(f"{prefix}└── [ACCESS DENIED]")
    except Exception as e:
        lines.append(f"{prefix}└── [ERROR: {str(e)}]")
    return lines

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Generate a text file with folder structure.')
    parser.add_argument('-d', '--directory', help='Target directory to analyze')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-g', '--gui', action='store_true', help='Use GUI dialogs to select directory and output file')
    args = parser.parse_args()

    # Determine target directory
    target_directory = None
    if args.gui or (not args.directory and len(sys.argv) == 1):
        print("Please select the folder to analyze...")
        target_directory = select_folder_dialog()
        if not target_directory:
            print("No folder selected. Exiting.")
            return
    elif args.directory:
        target_directory = args.directory
    else:
        # Default directory if no arguments provided
        target_directory = r"C:\Planet Projects"
    
    # Determine output file
    if args.gui or (not args.output and len(sys.argv) == 1):
        print("Please select where to save the folder structure...")
        output_file = select_output_file_dialog()
        if not output_file:
            print("No output file selected. Exiting.")
            return
    elif args.output:
        output_file = args.output
    else:
        # Default output file if no arguments provided
        output_file = os.path.join(os.path.expanduser("~"), "Desktop", "directory_tree.txt")

    # Ensure target directory exists
    if not os.path.isdir(target_directory):
        print(f"Error: The directory '{target_directory}' does not exist.")
        return

    # Generate the folder structure
    print(f"Analyzing folder structure of: {target_directory}")
    folder_structure_lines = list_directory_tree(target_directory)

    # Get current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the folder structure to the output file using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Folder structure of: {target_directory}\n")
        f.write(f"Generated on: {current_datetime}\n\n")
        for line in folder_structure_lines:
            f.write(line + '\n')

    print(f"Folder structure has been saved to: {output_file}")

    # Open the output file in Notepad++ if available
    notepad_plus_plus_path = r"C:\Program Files\Notepad++\notepad++.exe"
    if os.path.exists(notepad_plus_plus_path):
        subprocess.run([notepad_plus_plus_path, output_file])
    else:
        # Try to open with default text editor
        try:
            os.startfile(output_file)
        except:
            print("Could not open the output file automatically. Please open it manually.")

if __name__ == "__main__":
    main()
