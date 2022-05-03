# Python has 5 types of data types : Numbers, Strings, Boolean, Sequences, Dictionaries

myint = 5
myfloat = 5.5
mystr = "This is a string"
mybool = True
mylist = [1, 2, 'three', False]
mytuple = (1, 2, 3)
mydict = {'a': 1, 'b': 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# Re-declaring existing variable
myint = 'abc'
print(myint)

# to access a sequence list or tuple
print(mylist[2])
print(mytuple[2])

# use slices to get parts of a sequence
# mylist[startindex: endindex: step]
print(mylist[1:4])
print(mylist[1:4:2])

# use slice to reverse the sequence
# mylist[defaultstartindex:degaultendindex: step in reverse direction]
print(mylist[::-1])

# dictionaries are accessed by keys
print(mydict['a'])

# varibles of different types cannot be combined - error of type
# use str() to convert non string type to concatenate
print(mystr + str(myfloat))

# Global vs local variables in functions
# variable declared within function have function scope
# use global before variable name to update the variable in global scope
def someFunction():
    global mystr
    mystr = 'function'
    print(mystr)

someFunction()
print(mystr)

# delete the variable using del
del mystr
print(mystr)