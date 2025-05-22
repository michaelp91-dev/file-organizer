import os
import shutil

def organize_files(directory_path):
    """
    Organizes files in the given directory into subfolders based on file type.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found or is not a directory.")
        return

    print(f"\n--- Organizing files in: {directory_path} ---")

    # Define common file types and their target folders
    # You can expand/customize this dictionary as needed!
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
        'Audio': ['.mp3', '.wav', '.ogg', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.cs', '.json'], # Added .json for common data files
        'Others': [] # For files that don't match any specific type
    }

    # Create subfolders if they don't exist
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory_path, folder_name)
        os.makedirs(folder_path, exist_ok=True) # exist_ok=True prevents error if folder already exists

    # Iterate over files in the directory
    for filename in os.listdir(directory_path):
        # Skip directories themselves and the newly created type folders
        if os.path.isdir(os.path.join(directory_path, filename)):
            continue # Skip subdirectories (including the ones we just created)

        # Skip the script itself if it's in the target directory
        if filename == os.path.basename(__file__):
            continue

        file_extension = os.path.splitext(filename)[1].lower() # Get extension and convert to lowercase
        source_path = os.path.join(directory_path, filename)
        moved = False

        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                destination_path = os.path.join(directory_path, folder_name, filename)
                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved '{filename}' to '{folder_name}'")
                    moved = True
                    break # Break inner loop, move to next file
                except shutil.Error as e:
                    print(f"Error moving '{filename}': {e}. Skipping.")
                    moved = True # Consider it 'handled' even if error, to avoid 'Others'
                    break
        
        if not moved and file_extension: # If not moved and has an extension
             # Move to 'Others' if not matched by specific types
             destination_path = os.path.join(directory_path, 'Others', filename)
             try:
                 shutil.move(source_path, destination_path)
                 print(f"Moved '{filename}' to 'Others'")
             except shutil.Error as e:
                print(f"Error moving '{filename}' to 'Others': {e}. Skipping.")


def rename_files_sequential(directory_path, prefix="file_", start_num=1):
    """
    Renames files in the given directory with a sequential prefix.
    Example: file_1.jpg, file_2.png
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found or is not a directory.")
        return

    print(f"\n--- Renaming files in: {directory_path} ---")
    
    # Get only files, sort them to ensure consistent numbering every run
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    file_list.sort() 

    current_num = start_num
    for filename in file_list:
        old_path = os.path.join(directory_path, filename)
        name, ext = os.path.splitext(filename) # Separates 'filename' from '.ext'
        
        new_filename = f"{prefix}{current_num}{ext.lower()}" # Ensure consistent lowercase extension
        new_path = os.path.join(directory_path, new_filename)

        # Handle potential name conflicts (e.g., if new_filename already exists)
        counter = 0
        original_new_filename = new_filename
        while os.path.exists(new_path):
            counter += 1
            new_filename = f"{prefix}{current_num}_{counter}{ext.lower()}"
            new_path = os.path.join(directory_path, new_filename)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
            current_num += 1
        except OSError as e:
            print(f"Error renaming '{filename}': {e}. Skipping.")


def main():
    """
    Main function to run the script.
    Asks the user for the directory path and desired action.
    """
    print("\n--- Python File Organizer & Renamer CLI Tool ---")
    
    # Prompt for directory, provide example for Termux
    target_directory = input("Enter the directory path to operate on (e.g., /sdcard/Download or ~/storage/shared/my_test_folder): ")
    # Expand ~ to full path for Termux
    if target_directory.startswith('~'):
        target_directory = os.path.expanduser(target_directory)

    while True:
        print("\nChoose an action:")
        print("1. Organize files by type (creates subfolders)")
        print("2. Rename files sequentially (adds prefix + number)")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            organize_files(target_directory)
        elif choice == '2':
            prefix = input("Enter the new file prefix (e.g., 'myphoto_'): ")
            try:
                start_num = int(input("Enter the starting number for sequential naming (e.g., 1): "))
            except ValueError:
                print("Invalid starting number. Using 1.")
                start_num = 1
            rename_files_sequential(target_directory, prefix, start_num)
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
