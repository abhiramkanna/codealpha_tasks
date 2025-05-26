
import os
import shutil

# Define file type categories
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Programs": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh"],
    "Others": []
}

# Get the path to the folder you want to organize
folder_path = input("Enter the folder path to organize: ")

# Create folders based on file types
def create_folders():
    for category in file_types.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

# Organize files into respective folders
def organize_files():
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if file_name.endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(folder_path, category, file_name))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(folder_path, "Others", file_name))

# Main function to execute the script
def main():
    create_folders()
    organize_files()
    print("Files have been organized successfully!")

if __name__ == "__main__":
    main()
