"""
This code implements Randomized Quicksort, a variant of Quicksort that randomly selects a pivot to reduce the 
chance of worst-case performance (O(n^2)). It includes:

1. `randomized_quicksort`: Recursively sorts the array by partitioning around a random pivot.
2. `randomized_partition`: Selects a random pivot and partitions the array.
3. `partition`: Rearranges the array so elements smaller than the pivot are on the left, and larger ones on the right.
4. `test_randomized_quicksort`: Tests the algorithm on various edge cases (empty, sorted, reverse-sorted, repeated elements, random array).

Average time complexity: O(n log n).
"""
import random

# Randomized Quicksort function
def randomized_quicksort(arr, low, high):
    # Base case: If subarray size is 1 or 0, it is already sorted
    if low < high:
        # Get the pivot index using randomized partitioning
        pivot_index = randomized_partition(arr, low, high)
        # Recursively sort elements before and after the partition
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Randomized Partition function
def randomized_partition(arr, low, high):
    # Choose a random pivot index uniformly from the subarray
    pivot_index = random.randint(low, high)
    # Swap the randomly chosen pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # Partition the array around the pivot
    return partition(arr, low, high)

# Standard Partition function
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Pointer for elements smaller than pivot
    for j in range(low, high):
        # Move elements smaller than pivot to the left
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the pivot index

# Test function to handle edge cases and print arrays before and after sorting
def test_randomized_quicksort():
    # Case 1: Empty array
    arr_empty = []
    print(f"Before sorting empty array: {arr_empty}")
    randomized_quicksort(arr_empty, 0, len(arr_empty) - 1)
    print(f"After sorting empty array: {arr_empty}\n")
    
    # Case 2: Already sorted array
    arr_sorted = [1, 2, 3, 4, 5]
    print(f"Before sorting already sorted array: {arr_sorted}")
    randomized_quicksort(arr_sorted, 0, len(arr_sorted) - 1)
    print(f"After sorting already sorted array: {arr_sorted}\n")
    
    # Case 3: Reverse-sorted array
    arr_reverse = [5, 4, 3, 2, 1]
    print(f"Before sorting reverse-sorted array: {arr_reverse}")
    randomized_quicksort(arr_reverse, 0, len(arr_reverse) - 1)
    print(f"After sorting reverse-sorted array: {arr_reverse}\n")
    
    # Case 4: Array with repeated elements
    arr_repeated = [2, 2, 2, 2, 2]
    print(f"Before sorting array with repeated elements: {arr_repeated}")
    randomized_quicksort(arr_repeated, 0, len(arr_repeated) - 1)
    print(f"After sorting array with repeated elements: {arr_repeated}\n")
    
    # Case 5: Random array
    arr_random = [12, 3, 5, 7, 19, 4]
    print(f"Before sorting random array: {arr_random}")
    randomized_quicksort(arr_random, 0, len(arr_random) - 1)
    print(f"After sorting random array: {arr_random}\n")

# Run tests
test_randomized_quicksort()
