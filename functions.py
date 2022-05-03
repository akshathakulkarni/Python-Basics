# Define a simple function
def myFunction():
    print('Executing myFunction')

def myFunction2(arg1, arg2):
    print(arg1, arg2)
    return arg1

def square(x):
    return x*x

# Function that takes default value for argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result*num
    return result
# Function that takes variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

myFunction()
print(myFunction2('x', 'y'))
print(square(3))
print(power(2, 2))
print(power(x=2, num=3))
print(multi_add(4, 5, 10))