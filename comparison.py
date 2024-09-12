import time
import numpy as np
from main import partition, quicksort, randomized_quicksort, randomized_partition

def deterministic_quicksort(arr):
    quicksort_deterministic(arr, 0, len(arr) - 1)

def quicksort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_deterministic(arr, low, pi - 1)
        quicksort_deterministic(arr, pi + 1, high)

# Timing and comparing
def compare_algorithms():
    input_sizes = [100, 1000, 10000]
    for size in input_sizes:
        arr = np.random.randint(0, 10000, size)

        # Randomized Quicksort
        start = time.time()
        quicksort(arr.copy())
        print(f"Randomized Quicksort for {size} elements: {time.time() - start:.6f} seconds")

        # Deterministic Quicksort
        start = time.time()
        deterministic_quicksort(arr.copy())
        print(f"Deterministic Quicksort for {size} elements: {time.time() - start:.6f} seconds")

# Run the comparison when the script is executed
if __name__ == "__main__":
    compare_algorithms()

