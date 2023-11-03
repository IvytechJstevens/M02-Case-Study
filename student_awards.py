# Author: [Jace Stevens]
# File Name: student_awards.py
# Description: This Python app accepts student names and GPAs and determines if a student qualifies for either the Dean's List or the Honor Roll.

def main():

    # Initialize an empty list to store student information
    students = []

    # Define the number of students to process
    num_students = 5


    for _ in range(num_students):
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
        if last_name == 'ZZZ':
            break  # Exit the loop if 'ZZZ' is entered
    
        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))
    
        students.append({'first_name': first_name, 'last_name': last_name, 'gpa': gpa})

    # Check Dean's List and Honor Roll qualifications
    for student in students:
        if student['gpa'] >= 3.5:
            print(f"{student['first_name']} {student['last_name']} has made the Dean's List.")
        elif student['gpa'] >= 3.25:
            print(f"{student['first_name']} {student['last_name']} has made the Honor Roll.")

while True:
    main()
    # Option to repeat program if there are more students to record GPA's for.
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
