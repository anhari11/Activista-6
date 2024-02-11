def min_split_difference_arrays(arr):
    total_sum = sum(arr)
    min_difference = float('inf')
    current_sum = 0
    split_index = -1

    for i, num in enumerate(arr[:-1]):
        current_sum += num
        difference = abs(total_sum - 2 * current_sum)
        if difference < min_difference:
            min_difference = difference
            split_index = i

    # Return the two subarrays
    array1 = arr[:split_index + 1]
    array2 = arr[split_index + 1:]

    return array1, array2

arr = [8, 15, 10, 20, 8]
result1, result2 = min_split_difference_arrays(arr)
print(result1)
print(result2)
