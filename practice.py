# SUM OF NATURAL NUMBER USING RECURSION

def list_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + list_sum(arr[1 :])

numbers = [1,2,3,4,5]
print(list_sum(numbers))


# FACTORIAL OF A NUMBER

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


num = 5
print (factorial(num))

# FIBONACCI SERIES USING RECURSION 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i),end="  ")

print()


