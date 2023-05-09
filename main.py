from datetime import date
import os



today = date.today()
print("Today's date:", today)


# get the current working directory
cwd = os.getcwd()

# list all files and folders in the current directory
for file_name in os.listdir(cwd):
    print(file_name)


