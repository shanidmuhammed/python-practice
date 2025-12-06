# Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.

import zipfile

def zip_files(zip_file_name, *files):
    with zipfile.ZipFile(zip_file_name, "w") as z:
        for file in files:
            z.write(file)

zip_files('foo.zip', 'hui.txt', 'problem-1.py')