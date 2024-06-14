def computeProductArray(nums, size):

    # Base case
    if size == 1:
        print(0)
        return

    # Initialize memory for temporary arrays left_products and right_products
    left_products = [0] * size
    right_products = [0] * size

    # Initialize memory for the product array
    product_array = [0] * size

    # The leftmost element of left_products is always 1
    left_products[0] = 1

    # The rightmost element of right_products is always 1
    right_products[size - 1] = 1

    # Construct the left_products array
    for i in range(1, size):
        left_products[i] = nums[i - 1] * left_products[i - 1]

    # Construct the right_products array
    for j in range(size - 2, -1, -1):
        right_products[j] = nums[j + 1] * right_products[j + 1]

    # Construct the product_array using left_products and right_products
    for i in range(size):
        product_array[i] = left_products[i] * right_products[i]

    # Print the constructed product array
    for i in range(size):
        print(product_array[i], end=' ')


numbers = [10, 3, 5, 6, 2]
length = len(numbers)
print("The product array is:")
computeProductArray(numbers, length)
