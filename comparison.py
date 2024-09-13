"""
This comparison.py compares the performance of Iterative Randomized Quicksort and Iterative Deterministic Quicksort on different input distributions: 
randomly generated arrays, already sorted arrays, reverse-sorted arrays, and arrays with repeated elements. 
Iterative Randomized Quicksort selects a random pivot for each partition, while Iterative Deterministic Quicksort always selects the first element as the pivot.

NOTE: (Had to use Iterative method because I was getting RecursionError in Randomized quickSort, hitting python's recursion limit).

also observe and analyze the differences in running times, especially in edge cases like sorted and reverse-sorted arrays where 
Deterministic Quicksort may experience poor performance due to unbalanced partitions. 
Randomized Quicksort is expected to maintain consistent performance because of its randomized pivot selection, avoiding worst-case behavior.
"""

import random
import time

# Iterative Randomized Quicksort with random pivot
def randomized_quicksort_iterative(arr, low, high):
    # Create an auxiliary stack to simulate recursion
    stack = [(low, high)]

    # Pop from the stack while there are elements
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = randomized_partition(arr, low, high)  # Random pivot partition
            # Push subarrays to stack (larger side first to avoid deep recursion)
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

# Randomized partition (selects a random pivot and places it at the beginning)
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Randomly select pivot
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]  # Swap with the first element
    return partition(arr, low, high)

# Standard partitioning (first element as pivot)
def partition(arr, low, high):
    pivot = arr[low]  # Now the pivot is the first element
    i = low + 1  # Start from the next element
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Place the pivot at its correct position
    return i - 1  # Return the pivot index

# Iterative Deterministic Quicksort with first element as pivot
def deterministic_quicksort_iterative(arr, low, high):
    # Create an auxiliary stack to simulate recursion
    stack = [(low, high)]

    # Pop from the stack while there are elements
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)  # Partition using first element as pivot

            # Push subarrays to stack (larger side first to avoid deep recursion)
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

# Function to compare Iterative Randomized Quicksort and Iterative Deterministic Quicksort
def compare_algorithms():
    input_sizes = [100, 1000, 5000, 10000]  # Different input sizes
    
    for size in input_sizes:
        print(f"\nInput Size: {size}")
        # Generate different types of arrays
        arr_random = [random.randint(0, 10000) for _ in range(size)]
        arr_sorted = sorted(arr_random)
        arr_reverse = arr_sorted[::-1]  # Reverse-sorted array
        arr_repeated = [random.choice([1, 2, 3]) for _ in range(size)]  # Repeated elements

        # Iterative Randomized Quicksort
        for arr, name in [(arr_random.copy(), "Random Array"),
                          (arr_sorted.copy(), "Sorted Array"),
                          (arr_reverse.copy(), "Reverse Array"),
                          (arr_repeated.copy(), "Repeated Elements")]:
            start_time = time.time()
            randomized_quicksort_iterative(arr, 0, len(arr) - 1)
            print(f"Randomized Quicksort (Iterative) - {name}: {time.time() - start_time:.6f} seconds")

        # Iterative Deterministic Quicksort (First element as pivot)
        for arr, name in [(arr_random.copy(), "Random Array"),
                          (arr_sorted.copy(), "Sorted Array"),
                          (arr_reverse.copy(), "Reverse Array"),
                          (arr_repeated.copy(), "Repeated Elements")]:
            start_time = time.time()
            deterministic_quicksort_iterative(arr, 0, len(arr) - 1)
            print(f"Deterministic Quicksort (First Element, Iterative) - {name}: {time.time() - start_time:.6f} seconds")

# Run the comparison
compare_algorithms()
