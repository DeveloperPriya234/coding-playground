def insertion_sort(arr):
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at the correct position
        arr[j + 1] = key

    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
