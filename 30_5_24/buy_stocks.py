# List of prices
prices = [6, 1, 2, 4, 5, 6]
# Initialize 'buy' with the first price in the list
buy = prices[0]
# Initialize 'MAX_PROFIT' to 0
MAX_PROFIT = 0
# Get the number of elements in the prices list
n = len(prices)

# Loop through the list starting from the second element
for i in range(1, n):
    # If the current price is lower than the 'buy' price, update 'buy'
    if buy > prices[i]:
        buy = prices[i]
        # Print the new 'buy' price for debugging
        print(buy)
    # Otherwise, if the difference between the current price and 'buy' is greater than 'MAX_PROFIT', update 'MAX_PROFIT'
    elif prices[i] - buy > MAX_PROFIT:
        MAX_PROFIT = prices[i]
        
# Print the maximum profit for debugging
print(MAX_PROFIT)
