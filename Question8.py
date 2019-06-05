# Write a Python program to print the word for alphabet 'B' with any pattern like stars, dots, lines,etc. for the given input.
x= 9
y= 9
for a in range(0,x):
    for b in range(0,y):
        if(a == int(x/2) or a==0 or a == x-1 or b==0):
            if(b!=y-1):
                print("B",end="")
        else:
            print(" ",end="")
    print("B")