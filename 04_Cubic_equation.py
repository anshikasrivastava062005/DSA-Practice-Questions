'''Write a function to solve the following equation a³ + a²b + 2a²b + 2ab² + ab² + b³.
Write a program to accept three values in order of a, b and c and get the result of the above equation.
'''
def equation(a, b):
    result = a**3 + a**2*b + 2*a**2*b + 2*a*b**2 + a*b**2 + b**3
    return result


# taking inputs
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))   # accepted but not used in equation

# calling function
ans = equation(a, b)

print("Result:", ans)