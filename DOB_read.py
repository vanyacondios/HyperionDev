# Task 17 - Read from file and to specified format.

print("\nName")
with open('DOB.txt', 'r') as file:
    for i in file:
        j = i.split()
        print(" ".join(j[0:2]))

print("\nBirthdate")
with open('DOB.txt', 'r') as file:  
    for i in file:
        j = i.split()
        print(" ".join(j[2:]))


