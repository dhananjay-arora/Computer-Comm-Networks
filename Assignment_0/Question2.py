# Write a program that asks the user to enter their name and their age. Print a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime
name = input("Enter Your Name: ")
age = int(input( "Age, please: "))
thisYear = datetime.now().year
print(name,", you will turn 100 years old in year ",thisYear+(100-age))