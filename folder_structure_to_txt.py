import os
import subprocess

# Define the target directory and output file path
target_directory = r"C:\Planet Projects"
output_file = r"C:\Users\PiotrPlachta\Desktop\directory_tree.txt"

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
    return lines

# Generate the folder structure
folder_structure_lines = list_directory_tree(target_directory)

# Write the folder structure to the output file using UTF-8 encoding
with open(output_file, 'w', encoding='utf-8') as f:
    for line in folder_structure_lines:
        f.write(line + '\n')

print(f"Folder structure has been saved to: {output_file}")

# Open the output file in Notepad++ if available
notepad_plus_plus_path = r"C:\Program Files\Notepad++\notepad++.exe"
if os.path.exists(notepad_plus_plus_path):
    subprocess.run([notepad_plus_plus_path, output_file])
else:
    print("Notepad++ not found at the specified path. Please check the installation.")
