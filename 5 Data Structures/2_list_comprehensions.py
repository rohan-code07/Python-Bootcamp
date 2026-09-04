# Create a list containing the table of 5

# table = []

# for i in range(1,11):
#     table.append(5*i)

# print(table)
 

# list comprehensions(Effient list creation)

table = [5*i for i in range (1,11)]
print(table)

square = [x*2 for x in range (1,5)]
print(square)

sum = [i+3 for i in range (1,6)]
print(sum)