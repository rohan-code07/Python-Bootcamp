#MAP

numbers = [1, 2, 3, 4, 5, 6]

def square(x):
    return x**2

squared = list(map(square, numbers))
print(squared) 



#FILTER

# def greater_than_7(x):
#     if x>7:
#         return True
#     else:
#         return False
x = [1,34,45,3,52,33,2,4,22,4,23,34,3]
new = list(filter(lambda x:x>7, x))
print(new)



#REDUCE
from functools import reduce
digit = [3, 5, 8, 4, 9, 6]
      # [8, 8, 4, 9, 6]
      # [16, 4, 9, 6]
      # [20, 9, 6]
      # [29, 6]
      # [35]
def sum(a, b):
    return a + b
summed = reduce(sum, digit)
print(summed)


