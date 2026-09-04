  # Break :

# The break statement is used to exit a loop prematurely.

for i in range(1, 21):
    if i == 11:
        break    # Cancel the execution of loop
    print(i)  

# Continue :

# The continue statement skips the rest of the code in the current iteration and moves to the next iteration.

for i in range(1, 21):
    if i == 12:
        continue      # skips
    print(i)


# Pass : 

# The pass statement is a placeholder that does nothing. It is used when syntax requires a statement but no action is needed.

for i in range(10):
    if i == 5:
        pass     # Do nothing
    print(i)

print("End of the program")