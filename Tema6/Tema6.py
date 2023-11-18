# Create a Python script that does the following:
# -Takes a directory path and a file extension as command line arguments (use sys.argv).
# -Searches for all files with the given extension in the specified directory (use os module).
# -For each file found, read its contents and print them.
# -Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.
import os
import sys
def read_files_from_directory(path,extension):
    for file in os.listdir(path):
        if file.endswith(extension):
            try:
                with open(os.path.join(path,file),"r") as f:
                    print(f.read())
            except:
                print(f"Could not read file {file}")
# read_files_from_directory(sys.argv[1],sys.argv[2])

# Write a script using the os module that renames all files in a specified directory to have a sequential number prefix.
# For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or
# files that can't be renamed.

def rename_files_in_directory(path):
    os.chdir(path)
    files = os.listdir()
    for index,file in enumerate(files):
        try:
            os.rename(file,f"{file.split('.')[0]}{index+1}.txt")
        except:
            print(f"Could not rename file {file}")
            
# rename_files_in_directory("Test")

# Create a Python script that calculates the total size of all files in a directory provided as a command line argument.
# The script should:
# -Use the sys module to read the directory path from the command line.
# -Utilize the os module to iterate through all the files in the given directory and its subdirectories.
# -Sum up the sizes of all files and display the total size in bytes.
# -Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.

def total_size_of_files(path):
    total_size = 0
    for root,dirs,files in os.walk(path):
        for file in files:
            try:
                total_size += os.path.getsize(os.path.join(root,file))
            except:
                print(f"Could not read file {file}")
    print(f"Total size of files in {path} is {total_size} bytes")
    
total_size_of_files("Test")

# Write a Python script that counts the number of files with each extension in a given directory. The script should:
# -Accept a directory path as a command line argument (using sys.argv).
# -Use the os module to list all files in the directory.
# -Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# -Include error handling for scenarios such as the directory not being found, no read permissions,
# or the directory being empty.

def count_files_by_extension(path):
    counts = {}
    for root,dirs,files in os.walk(path):
        for file in files:
            extension = file.split(".")[-1]
            if extension not in counts:
                counts[extension] = 1
            else:
                counts[extension] += 1
    for extension,count in counts.items():
        print(f"{extension} files: {count}")
        
count_files_by_extension("Test")