'''Pythagorean Triplets:
Problem: Generate all Pythagorean triplets with values smaller than a given limit.
Input: limit = 20
Output:
3 4 5
8 6 10
5 12 13
15 8 17
12 16 20
Explanation: The triplets satisfy the condition a² + b² = c², where a, b, and c are integers.'''

def pythagorean_triplets(limit):
    for c in range (1,limit+1):
        for a in range (1,c):
            for b in range (a,c):
                if a*a + b*b == c*c:
                    print(a,b,c)

#example
pythagorean_triplets(20)