# Command-Line File Organizer & Renamer

A simple yet powerful Python script designed to automate common file management tasks directly from the command line. This tool helps users organize their cluttered directories by categorizing files into type-based subfolders and offers a flexible sequential renaming utility.

## Features

-   **Organize Files by Type:** Automatically moves files into categorized subfolders (e.g., `Images`, `Documents`, `Videos`, `Code`, `Archives`, `Audio`, `Others`). Customizable file types.
-   **Sequential Renaming:** Renames files in a specified directory with a custom prefix and sequential numbering, avoiding name conflicts.
-   **User-Friendly CLI:** Interactive command-line interface makes it easy to choose actions and provide necessary inputs.
-   **Error Handling:** Includes checks for invalid directory paths and provides informative messages.

## Technologies Used

-   **Python:** The core language for the script.
-   **Standard Libraries:** `os` (for operating system interaction, path manipulation) and `shutil` (for high-level file operations like moving).

## How to Use

1.  **Prerequisites:** Ensure you have Python installed on your system (e.g., Termux on Android, Python on Linux/macOS/Windows).
2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/michaelp91-dev/file-organizer.git
    cd file-organizer
    ```
    (Replace `YOUR_GITHUB_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and the repository name you chose)
3.  **Run the Script:**
    ```bash
    python organizer.py
    ```
4.  **Follow Prompts:** The script will ask you to enter the target directory path (e.g., `/sdcard/Download` or `~/storage/shared/my_test_folder`) and choose an action.

**Important Note:**
**Always test this script on a *copy* of your important files first!** Accidental deletion or misplacement of files can occur if the directory path is incorrect or if the script logic is not fully understood.

## Example Usage (in terminal)

```bash
$ python organizer.py
--- Python File Organizer & Renamer CLI Tool ---
Enter the directory path to operate on (e.g., /sdcard/Download or ~/storage/shared/my_test_folder): /home/user/my_downloads

Choose an action:
1. Organize files by type (creates subfolders)
2. Rename files sequentially (adds prefix + number)
3. Exit
Enter your choice (1/2/3): 1

--- Organizing files in: /home/user/my_downloads ---
Moved 'image.jpg' to 'Images'
Moved 'report.pdf' to 'Documents'
Moved 'video.mp4' to 'Videos'
Moved 'script.py' to 'Code'
# ... (and so on)
