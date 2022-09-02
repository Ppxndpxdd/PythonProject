def factorial(input):
    if input == 1:
        return input
    elif input == 0:
        return 1
    else:
        return input*factorial(input-1)

inp = int(input("Enter Number : ")) 
print(str(inp) + "!" + " = "+ str(factorial(inp)))
