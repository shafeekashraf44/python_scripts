# Prompt the user to enter the number of stairs
stairs = int(input("Enter the number of stairs:"))

# Check if the number of stairs is less than or equal to 1
if stairs <= 1:
    # If it is, print the number of stairs and exit
    print(stairs)
else:
    # Calculate the sum of (stairs - 1) and (stairs - 2)
    # This seems to be a step towards computing the Fibonacci sequence which is used in the "staircase problem"
    result = (stairs - 1) + (stairs - 2)
    # Print the result
    print(result)
