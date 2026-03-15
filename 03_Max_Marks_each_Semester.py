'''Raj wants to know the maximum marks scored by him in each semester. The mark should be between
0 to 100; if it goes beyond the range display “You have entered invalid mark.”
Sample Input 1:
Enter no of semester: 3
Enter no of subjects in 1 semester: 3
Enter no of subjects in 2 semester: 4
Enter no of subjects in 3 semester: 2
Marks obtained in semester 1: 50 60 70
Marks obtained in semester 2: 90 98 76 67
Marks obtained in semester 3: 89 76
Sample Output 1:
Maximum mark in 1 semester: 70
Maximum mark in 2 semester: 98
Maximum mark in 3 semester: 89
'''
semesters = int(input("Enter no of semester: "))

subjects = []

# taking number of subjects in each semester
for i in range(semesters):
    n = int(input(f"Enter no of subjects in {i+1} semester: "))
    subjects.append(n)

# processing marks
for i in range(semesters):
    marks = list(map(int, input(f"Marks obtained in semester {i+1}: ").split()))
    
    if len(marks) != subjects[i]:
        print("Invalid number of marks entered.")
        continue

    invalid = False
    
    for m in marks:
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            invalid = True
            break
    
    if not invalid:
        print(f"Maximum mark in {i+1} semester:", max(marks))