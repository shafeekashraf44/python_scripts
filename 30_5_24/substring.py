def longestUniqueSubsttr(str):
    n = len(str)
    res = 0
    # Iterate over each character in the string
    for i in range(n):
        # Initialize the visited array to keep track of characters in the current window
        visited = [0] * 256
        for j in range(i, n):
            # If the character is already visited, break the loop
            if visited[ord(str[j])] == True:
                break
            else:
                # Update the result if the current window is larger
                res = max(res, j - i + 1)
                # Mark the character as visited
                visited[ord(str[j])] = True
        # Reset the first character of the current window as not visited
        visited[ord(str[i])] = False
    return res

str = "abcabcdef"
# Get the length of the longest substring with all unique characters
len = longestUniqueSubsttr(str)
print(len)
