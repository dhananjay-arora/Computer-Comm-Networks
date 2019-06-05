# Write a function to print all student names and date of birth on the student records using FOR loop.
def student_data():
    student_list = {
    'firstName' : ['Henry', 'Owen', 'Calder', 'Alexander', 'Olivia', 'Felicity', 'Amelia', 'Harrison', 'Stella', 'Brad' ],
    'lastName' : ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Verma', 'Davis', 'Miller', 'Wilson', 'Pitt'],
    'dateOfBirth' : ['01/02/1990','02/12/1990', '03/13/1990', '04/14/1990', '05/16/1990', '06/18/1990', '07/19/1990', '08/27/1990', '09/28/1990', '10/30/1990']}
    print("Below is the list of students")
    for x in range(0,(len(student_list[list(student_list.keys())[0]]))):
        for y in student_list:
            data = student_list[y][x]
            print('{:<14s}'.format(data),end="")
        print("")
student_data()