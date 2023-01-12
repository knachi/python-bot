# Import os module to check the existence of the file
import os


# Drfine function check the file is closed or not
def check_closed():
    if not fileHandler.closed:
        # Print the success message
        print("File has opened for reading.")
    else:
        # Print the error message
        print("File has closed.")


# Take the filename to check
# filename = input("Enter any existing filename:\n")
filename = 'home/file/file1.txt'
# Check the file exist or not
if os.path.exists(filename):
    # Open the file for reading
    fileHandler = open(filename, "r")
    # Call the function
    check_closed()
else:
    # Print message if the file does not exist
    print("File does not exist.")
