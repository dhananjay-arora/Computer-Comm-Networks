# Write a decorator function that takes the student name as arguement and creates an emailID ID for the student using first 2 letters of first & last name.
def  decorator(name):
    name = name.lower()
    firstName = name[:2]
    lastName = name.split(' ')[1][:2]
    return firstName+lastName+"@example.com"
emailID = decorator(input("Enter your complete name (first name and last name) \n"))
print("Email ID is "+emailID)