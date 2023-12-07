
"""
    Get-All-User-Files.py
    @author Lehrman, Aidin
    
    Gets all user files, prints them out, and also puts them in a folder.
    
    ---
    
    To Run:
        1. Install Python (v.3.10.11) if not already installed.
            - https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

        2. Run Python file in PowerShell.
            - python C:/Users/<UserName>/<Location>/Get-All-User-Files.py
            
        3. Rejoice.
            - Yay! You did it.
"""

import os
import time

extensions = [
    '.doc', '.docx', '.txt', '.pdf', '.htm', '.html', '.ppt', '.pptx',
    '.wma', '.avi', '.mov', '.jpg', '.jpeg', '.png', '.gif', '.psd',
    '.svg', '.ai', '.zip', '.rar', '.7z', '.xlsx', '.rtf', '.exe', '.mp3',
    '.mp4', '.msi', '.dll', '.eps', '.', '.xls', '.cvn', '',
]

document_location_paths = [
    '3D Objects', 'Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos',
]

def welcome_message():
    print('*' * 43 + '\n*             FOR CYBER PATRIOTS          *\n' + '*' * 43)
    print('\nThis python file gets all user files on the\ncomputer to help find hidden files a user\nmay have\n')
    for seconds in range(5, 0, -1):
        print(f'\rThis script will now execute in {seconds} seconds', end=('' if seconds > 1 else '\n\n'))
        time.sleep(1)

def get_user_list():
    user_home = os.path.expanduser('~')
    return user_home.replace('C:\\Users\\', '')

def get_files():
    list_of_files = [
        os.path.join(root, file)
        for ending in document_location_paths
        for root, dirs, files in os.walk(os.path.join('C:/Users/', get_user_list(), ending))
        for file in files
        if file.endswith(tuple(extensions))
    ]
    return list_of_files

def write_files_to_text(files):
    try:
        with open("User_Files.txt", 'w') as f:
            f.write('\n'.join(files))
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    welcome_message()
    
    user_list = get_user_list()
    print(f'All files found under users: {user_list}\n')
    
    list_of_files = get_files()

    write_files_to_text(list_of_files)

    for name in list_of_files:
        print(name)

if __name__ == "__main__":
    main()
