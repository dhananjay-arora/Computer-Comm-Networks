#Write a program to list all the files in the given directory along with their length and last modification time. 
#The output should contain one line for each file containing filename, length and modification date separated by tabs.
import os
import datetime as date
from texttable import Texttable
path = input("Enter the address of directory:")
text = Texttable()
headers = ["File Name","File Size", "Last Modified Date"]
text.header(headers)
for file in os.scandir(path):
    if file.is_file():
        modifiedTime = os.path.getmtime(file)
        file = [file.name,os.path.getsize(file),date.datetime.fromtimestamp(modifiedTime)]
        text.add_row(file)
print(text.draw())