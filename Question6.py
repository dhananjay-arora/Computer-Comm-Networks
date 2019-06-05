# Write a Python program to demonstrate that a function can be defined inside another function and a function can be passed as parameter.
def outerFunction(parameter):
    def innerFunction(parameter):
        print(parameter)
    innerFunction(parameter)
def function(outerFunction,parameter):
    outerFunction(parameter)
parameter= "Welcome to Python Programming"
function(outerFunction,parameter)