'''
Write the code to traverse a matrix in a spiral format.
Sample Input:
5 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
Output:
1 2 3 4 8 12 16 20 19 18 17 13 9 5 6 7 11 15 12 14 10
'''
rows, cols = map(int, input().split())

matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = rows - 1
left = 0
right = cols - 1

result = []

while top <= bottom and left <= right:

    # Traverse top row
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # Traverse right column
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        # Traverse bottom row
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        # Traverse left column
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)
