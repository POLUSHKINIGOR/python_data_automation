import os
import shutil

# Folder to clean up (current working directory)
source_folder = os.getcwd()
# Folder to move text files into
target_folder = os.path.join(source_folder, "txt_files")

# Create target folder if it doesn't exist
os.makedirs(target_folder, exist_ok=True)

# List all files in the source folder
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

txt_counter = 1
for file_name in files:
    if file_name.endswith(".txt"):
        # New file name
        new_file_name = f"text_file_{txt_counter}.txt"
        # Source and destination paths
        src_path = os.path.join(source_folder, file_name)
        dst_path = os.path.join(target_folder, new_file_name)
        # Move and rename file
        shutil.move(src_path, dst_path)
        txt_counter += 1

print(f"All .txt files have been moved to '{target_folder}' and renamed sequentially.")
