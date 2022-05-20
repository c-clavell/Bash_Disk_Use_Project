# Bash_Disk_Use_Project

Task 1: Prepare the Python Script.

Task 2: Use the __name__ to identify the main code and use sys.argv to access the command line arguments.      

Task 3: Create a for loop to access each sub-directory. Using the method os.scandir(path) that
returns a list of directories and files found inside the directory. 

Task 4: Create a function (get_size()) to determine the disk space used (bytes) by each 
directory. The directories paths are then recursively pass in to the function 
until all the file sizes are summed up.

Task 5: Use a python package to generate a report in CSV format.

I added more functionality to the function. Beside getting the total size, it will also
determine the total number of files and directories present inside the directory.

The default path will be the current working directory. You can use the os.getcwdb() method or use the 
subprocess.run method to run the bash command 'pwd' to get the working dir path.
