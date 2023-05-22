# Task 18 - Ask user to input number of students. Ask for consecutive input of ID number and write to file, including space for signature.

while True:
    try:
        number_of_students = input("How many students will be taking the exam? ")
        number_of_students = int(number_of_students)
        break
    except ValueError:
        print("Not a valid number, please enter a whole number larger than zero: ")
# Integer exception handling - https://python-course.eu/python-tutorial/errors-and-exception-handling.php

with open("reg_form.txt", "w+") as file:
    file.write("Register of Exam Candidates\n\n") 
    for i in range(number_of_students):
        id_number = input(f"Please enter the ID number of Student {i+1}: ")
        file.seek(0) 
        while id_number in file.read(): #validate against duplicate entries
            id_number = input("This student is already registered. Please enter another number: ")
        while id_number.isnumeric() != True or len(id_number) != 4:  # validate ID, assuming a 4 digit number format
            id_number = input("Please enter a valid student ID, these are numeric and consist of 4 digits: ")
        file.write(id_number + "\n\n....................................\n\n")
