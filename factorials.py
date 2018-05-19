__author__ = 'xhadix'

# calculate N with function
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

# but we can do with math.factorial(n) libs in python 

# read input as integer
numbs = int(input("insert number = "))
# call the function
print(factorial(numbs))