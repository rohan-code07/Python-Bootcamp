# Python provides powerful built in data structure to store and manipulate collection of data efiiciently


# LISTS

# lists are ordered, mutable(changable), collections of items.

marks = [34, 56, 78, 98, 67]
mixed = [34, "Rohan", False, 43.67]

print(marks)        # prints whole list
print(marks[2])     # prints single element of the list
print(mixed[1])     # prints single element of the list
print(marks[1:4])   # list slicing
# print(mixed[4])   # Error Index out of bound
marks[3] = 34       # change the value of element
print(marks)

# LIST  

lists = [2, 2, 5, False, 54]
extra_list = (45, 18)
print(lists)

lists.append(88)           # add the element at the end of the list
print(lists)

lists.copy()             # Return a shallow copy of the list.
print(lists)

print(lists.count(2))      # Return number of occurrences of value. 

lists.extend(extra_list)   # Extend list by appending elements from the iterable.
print(lists)

print(lists.index(54))     # Return first index of value.

lists.insert(1, 3.14)      # Insert object before index.   insert(index, element)
print(lists)

print(lists.pop(1))         # Remove and return item at index (default last).
print(lists)

lists.remove(2)            # Remove first occurrence of value.
print(lists)

lists.reverse()            # Reverse the list
print(lists)

lists.sort()               #  Sort the list in ascending order
print(lists)

lists.sort(reverse= True)  #  Sort the list in decending order
print(lists)

# rev_list = sorted(lists, reverse = True)   # returns new sorted list and leaves the original list unchanged
# print(lists)
# print(rev_list)
