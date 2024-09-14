# Assignment3: Understanding ALgorithm Efficiency and Scalability
This assignment contains implementations and analyzed reports for two key algorithms: **Randomized Quicksort** and **Hashing with Chaining**. The assignment focuses on analyzing and comparing the efficiency and scalability of these algorithms, providing both theoretical analysis and empirical results.

## Files in this Repository

### 1. `randomized_quicksort.py`
This [file](randomized_quicksort.py) contains the implementation of **Randomized Quicksort**, where the pivot is chosen randomly to reduce the likelihood of worst-case performance.

#### Running `randomized_quicksort.py`:
```ruby
python3 randomized_quicksort.py
```


### 2. `comparison.py`
This [file](./comparison.py) compares the performance of **Randomized Quicksort** and **Deterministic Quicksort** on different input arrays (random, sorted, reverse-sorted, and arrays with repeated elements).

#### Running `comparison.py`:
```ruby
python3 comparison.py
```

### 3. `hash_table_chaining.py`
This [file](hash_table_chaining.py) implements a hash table using **chaining** for collision resolution. It supports operations such as insert, search, and delete.

#### Running `hash_table_chaining.py`:
```ruby
python3 hash_table_chaining.py
```

### 4. `report_part1.md`
This [report](report_part1.md) provides a detailed analysis of the **Randomized Quicksort** algorithm, including its theoretical time complexity and empirical performance comparison with Deterministic Quicksort.


### 5. `report_part2.md`
This [report](report_part2.md) analyzes the performance of the **Hashing with Chaining** algorithm, focusing on the time complexity of search, insert, and delete operations, and discusses strategies for maintaining efficiency.

## Summary of the Assignment

### Part 1: Randomized Quicksort
The **Randomized Quicksort** algorithm is analyzed both theoretically and empirically. Randomization ensures that the average-case time complexity remains \(O(n log n)\), while Deterministic Quicksort suffers from \(O(n^2)\) behavior for already sorted or reverse-sorted arrays.

### Part 2: Hashing with Chaining
The **Hashing with Chaining** implementation is evaluated based on its performance in search, insert, and delete operations. We discuss the effect of the load factor on time complexity and the importance of using a good hash function to minimize collisions. Dynamic resizing is also recommended to keep the load factor low.

## Required Libraries
The code requires the following Python libraries:
- `random` (for generating random input arrays in `comparison.py` and `randomized_quicksort.py`)
- `time` (for benchmarking in `comparison.py`)

Feel free to explore the repository and run the files to see how each algorithm performs in different scenarios!