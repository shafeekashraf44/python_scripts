def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

LIST_1 = [1, 2, 7, 4, 5]
LIST_2 = [6, 7, 1, 3, 9]
# Combine both lists into a single list
final_list = LIST_1 + LIST_2
# Sort the combined list using selection sort
selection_sort(final_list)
# Print the sorted list
print(final_list)
