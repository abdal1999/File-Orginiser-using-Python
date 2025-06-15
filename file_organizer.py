import os
import shutil

SOURCE_FOLDER = "sample folder"

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Spreadsheets': ['.xlsx', '.csv'],
    'Videos': ['.mp4', '.mov'],
    'Archives': ['.zip', '.rar'],
    'Code': ['.py', '.js', '.html']
}

def organize_folder(source_path):
    if not os.path.exists(source_path):
        print("Source folder not found!")
        return

    for file in os.listdir(source_path):
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(source_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print("Moved", file)
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(source_path, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))
                print("Moved", file)

if __name__ == "__main__":
    organize_folder(SOURCE_FOLDER)
