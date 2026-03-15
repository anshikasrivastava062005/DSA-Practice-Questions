'''
Matrix Rotation by 90 Degrees:
Rotate a 2D matrix by 90 degrees clockwise.
Input: Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output:Matrix:[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Explanation: The matrix is rotated 90 degrees clockwise
'''

def rotate_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = rotate_matrix(matrix)

print("Matrix:", result)
