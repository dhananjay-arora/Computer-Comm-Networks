# Write a Python program to print the given string, where all occurrences of its first char should be been changed to '$’. 
# You should write your own function that takes the input string as argument and returns the string with the replaced character
def edit(argument):
    firstChar = argument[0]
    argument = firstChar + argument[1:].replace(firstChar, '$')
    return(argument)
argument = 'restart'
result = edit(argument)
print("Sample String :",argument)
print("Result :",result)