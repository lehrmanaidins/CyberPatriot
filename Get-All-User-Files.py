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

extentions = ['.doc', '.docx', '.txt', '.pdf', '.htm', '.html', '.ppt', '.pptx', '.wma', '.avi', '.mov', '.jpg', '.jpeg', '.png', '.gif', '.psd', '.svg', '.ai', '.zip', '.rar', '.7z', '.xlsx', '.rtf', '.exe', '.mp3', '.mp4']
document_location_paths: list[str] = ['Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos',]

def welcome_message():
    
    print( '*******************************************\n*             FOR CYBER PARTIOTS          *\n*******************************************\n')
    
    print('This python file gets all user files on the\ncomputer to help find hidden files a user\nmay have\n')
    
    # Virual machines for Cyber Patriots are very slow 
    # Allows the computer time to run the program
    for seconds in range(5, 0, -1):
        print(f'\rThis script will now execute in {seconds} seconds', end=('' if seconds > 1 else '\n\n'))
        time.sleep(1)


# Overview, Gets all users on the machine and prints them out

welcome_message()
users = []

# Strips the usernames of unnecessary parts
remove_content = ('C:\\Users\\' + '''[]'"''')
# Gets all usernames on the computer
users.append(os.path.expanduser('~'))
user_list = repr(users) # Turns list into str
for content in remove_content:
    user_list = user_list.replace(content, '')

print (f'All files found under users: {user_list}\n')


# Uses os.walk to find all files with extentions I want
list_of_files = []
for ending in document_location_paths:
    for root, directories, file in os.walk(f'C:/Users/{user_list}/{ending}'):
	    for file in file:
		    if(file.endswith(tuple(extentions))):
			    list_of_files.append(os.path.join(root,file))

# Creates file to put file list in
try:
    f = open("User_Files.txt", 'w')
    files = repr(list_of_files)
    f.write(files.replace(",", ", \n"))
    f.close()
except FileExistsError:
    print("File exist on the computer")


for name in list_of_files:
    print(name)
