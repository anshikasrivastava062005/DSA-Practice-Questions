'''
Matrix Identity Check:
Problem: Write a program to check if two given matrices are identical.
Input:
Matrix A: [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
Matrix B: [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
Output:
Matrices are identical
'''

A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

B = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

rows = len(A)
cols = len(A[0])

identical = True

for i in range(rows):
    for j in range(cols):
        if A[i][j] != B[i][j]:
            identical = False
            break
    if not identical:
        break

if identical:
    print("Matrices are identical")
else:
    print("Matrices are not identical")

    # second method 

A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

B = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

if A == B:
    print("Matrices are identical")
else:
    print("Matrices are not identical")