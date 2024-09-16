# Assignment3: Understanding ALgorithm Efficiency and Scalability
This assignment contains implementations and analyzed reports for two key algorithms: **Randomized Quicksort** and **Hashing with Chaining**. The assignment focuses on analyzing and comparing the efficiency and scalability of these algorithms, providing both theoretical analysis and empirical results.

## How to Run the Code

### Requirements:
- Python 3.x

### Running the Code:
1. Download the source code from the provided `.py` file or copy the provided code.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `.py` file is saved.
4. Run the Python script by typing the following command:
   for windows:
   ``` bash
   python filename.py
   ```
   for MacOS (or Linux):
   ``` bash
   python3 filename.py
   ```
   Replace `<filename>` with the actual name of the Python file.


## Files in this Repository

## Files Overview

| File Name                  | Description                                                                                  |
|----------------------------|----------------------------------------------------------------------------------------------|
| [randomized_quicksort.py](./randomized_quicksort.py)   | Implements **Randomized Quicksort** with a randomly chosen pivot to avoid worst-case performance. |
| [comparison.py](./comparison.py)             | Compares the performance of **Randomized Quicksort** and **Deterministic Quicksort** using various input arrays. |
| [hash_table_chaining.py](./hash_table_chaining.py)    | Implements a **Hash Table with Chaining** for collision resolution, supporting insert, search, and delete operations. |
| [report_part1.md](./report_part1.md)           | Detailed report analyzing the **Randomized Quicksort** algorithm's theoretical and empirical performance. |
| [report_part2.md](./report_part2.md)           | Detailed report analyzing the performance of the **Hashing with Chaining** algorithm, including time complexity analysis and optimization strategies. |

---


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
