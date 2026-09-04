# SETS

# Sets are unordered, unique collections (no duplicates).
# Sets are great for eliminating duplicate values.


set = { 2, 34, 23, 5}

print(set, type(set))

# print(set[3])  # you cannot do something like this


# SET METHODS


my_set = {1, 3, 5, 6, 8}

my_set.add(7)             # add a element randomly in set
print(my_set)

my_set.remove(3)          # Remove an element from a set; it must be a member.
print(my_set)

my_set.discard(5655)      # Remove an element from a set if it is a member.
print(my_set)             # does not throw  error like remove() when element is not present

my_set.pop()              # Remove a random element from the set.
print(my_set)


# SET OPERATIONS

a = {1, 2, 3, 4, 5}
b = {2, 3, 7, 8}
c = {1, 5, 6, 7}

print(a.difference(b))   # returns a new set containing elements that are in the first set but not in the other set(s).
print(a - b)             # works only for sets and works same as difference()

c.difference_update(b)    # Modifies the original set directly.
print(c)        
c -= b                    # works same as difference_update()
print(c)

print(a.symmetric_difference(b))  # elements in either the set but not both.
print(a ^ b)                      # works same as symmetric_difference()

# difference()         → gives a NEW set
# difference_update()  → UPDATES the existing set


print(a.intersection(b))  
print(a & b)              # works as intersection()

c.intersection_update(a)  
print(c)

# intersection()       → keep only common elements
# intersection_update() → keep only common elements and update the original set.
 

print(a.union(b))      
print(a | b)             # works same as union()

b.update(c)
print(b)                  

# union()        → combine all unique elements and return a new set
# update()       → combine all unique elements and update the original set

d = {3, 4}
e = {11, 12}

print(d.issubset(a))    # Check if one set is contained in another.  returns True or False

print(a.issuperset(d))   # Set if it contains all the elements of that another set. returns True or False

print(a.isdisjoint(e))   # Checks if two sets have no common elements. returns True or False

e.clear()                # Removes all the elements
print(e)


# A | B   # union
# A & B   # intersection
# A - B   # difference
# A -= B  # difference_update
# A ^ B   # symmetric difference
