# from array import *
from numpy import *

# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# for i in range(0, len(val)):
#     print(val[i], end=' ')
# print('\n')

# for x in val:
#     print(x, end=', ')
# print('\n')

# print(val.typecode)

# val.reverse()

# for x in val:
#     print(x, end=', ')

# val.insert(0, 0)
# val.append(11)

# val[2] = 21

# CopyArray = array(val.typecode, (x for x in val ))

# CopyArray.pop(1) #removes element based on index if not mentioned removes last element
# CopyArray.remove(4) #removes element based on value if index is not known

# Sliced_Array = val[2:5]

# Reverse_Array = val[::-1] #Alternative to reverse() method

# n = int(input('enter the number of elements you want to add: '))

# arr = array('i', [])

# for i in range(n):
#     x = int(input('enter the element: '))
#     arr.append(x)

# for x in arr:
#     print(x, end=' ')

# val = array([1, 2, 3, 4, 5, 6, 7.7, 8, 9, 10],  dtype=float)

# val = linspace(0, 15, 5) #start, stop(included), number of elements

# val = arange(0, 15, 2.5) #start, stop(excluded), step

# val = zeros(5) #array of 5 zeros
# val = ones(5) #array of 5 ones

val = full(5, 7) #array of 5 sevens

for i in range(0, len(val)):
    print(val[i], end=' ')
print('\n')

