print("="*40)
print("          Simple Calculator")
print("="*40)
history = []
try:
    while True:
        first = input("Enter first no.(or q to quit): ")
        if first.lower() == "q":
            break
        a = int(first)
        b = int(input("Enter second no.: "))
        
        op = input("Enter a operation: ")
        match op:
            case "+": result = a + b
            case "-": result = a - b
            case "*": result = a * b
            case "/":
                if b == 0:
                    continue
                else:
                    result = a / b
            case "**": result = a ** b
            case  _ : print("Invalid operation")
        print(f"{a} {op} {b} = {result}")
        history.append(f"{a} {op} {b} = {result}")


except ValueError:
    print("Enter the valid values")

print("-"*40)

print('='*40)
if history:
    for index, item in enumerate(history, start=1):
        print(f"{index}.{item}")

else:
    print("there is no calculation")

print('='*40)