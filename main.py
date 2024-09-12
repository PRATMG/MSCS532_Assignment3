import random

# Partition function to divide the array
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized partition function
def randomized_partition(arr, low, high):
    random_pivot_index = random.randint(low, high)
    arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]
    return partition(arr, low, high)

# Randomized Quicksort function
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Function to sort the array
def quicksort(arr):
    randomized_quicksort(arr, 0, len(arr) - 1)

# Test case to actually see the output
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    quicksort(arr)
    print("Sorted array:", arr)
