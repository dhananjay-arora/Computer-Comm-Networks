#You will keep track of when your friend’s birthdays are, and be able to find that information based on their name. 
#Create a dictionary of names and birthdays. 
#When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
dictionary={'friendName':[],'birthDate':[]}
dictionary['friendName'].append('Henry Smith')
dictionary['birthDate'].append('01/05/1989')
dictionary['friendName'].append('Owen Johnson')
dictionary['birthDate'].append('02/20/1980')
dictionary['friendName'].append('Rachael Green')
dictionary['birthDate'].append('03/15/1979')
dictionary['friendName'].append('Ross Geller')
dictionary['birthDate'].append('04/10/1970')
dictionary['friendName'].append('Chandler Bing')
dictionary['birthDate'].append('05/02/1969')
print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in dictionary['friendName']:
    print(i)
position = -1
name = input("Who's birthday do you want to look up? \n")
for x in range(0,len(dictionary['friendName'])):
    if dictionary['friendName'][x] == name:
        position = x
        date = dictionary['birthDate'][position]
        print()
        print(name + "'s birthday is", date)
        break
if position == -1:
    print("Wrong Name Entered")