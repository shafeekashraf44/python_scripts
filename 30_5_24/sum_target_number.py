input_string = [1, 2, 3, 4, 5]
target = int(input("Enter the target:"))
index_dict = {}



# Create a dictionary to map values to their indices
for index, value in enumerate(input_string):
    index_dict[value] = index

# Iterate over each value in the input list
for i in input_string:
    compare = (target - i)
    # Check if both the current value and the complement exist in the input list
    if all(variable in input_string for variable in [i, compare]):
        # Print the indices of the two numbers that add up to the target
        print(f"{index_dict[i]}, {index_dict[compare]}")
        break
