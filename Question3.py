# Write a program to store record of 10 students using Dictionary data type. Student record should hold Student first & last name and date of birth.
student_list = {
    'firstName' : ['Henry', 'Owen', 'Calder', 'Alexander', 'Olivia', 'Felicity', 'Amelia', 'Harrison', 'Stella', 'Brad' ],
    'lastName' : ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Verma', 'Davis', 'Miller', 'Wilson', 'Pitt'],
    'dateOfBirth' : ['01/02/1990','02/12/1990', '03/13/1990', '04/14/1990', '05/16/1990', '06/18/1990', '07/19/1990', '08/27/1990', '09/28/1990', '10/30/1990']}
print("Below is the dictionary having first name, last name and date of birth")
for x in range(0,(len(student_list[list(student_list.keys())[0]]))):
        for y in student_list:
            data = student_list[y][x]
            print('{:<10s}'.format(data),end="")
        print("")