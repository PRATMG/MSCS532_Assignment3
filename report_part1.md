
# Part 1: Randomized Quicksort Analysis
## Introduction
The average-case time complexity of Randomized Quicksort is O(nlogn). This is demonstrate by analyzing the expected number of comparisons made during the execution of the algorithm.
This report provides analysis of the average-case time complexity of the Randomized Quicksort algorithm, which is O(n log n). The analysis will use indicator random variables to demonstrate the expected number of comparisons performed during the execution of Randomized Quicksort.

- [Randomized Quicksort Implementation](./randomized_quicksort.py)

# Sorting Output

| **Array Type**                 | **Before Sorting**           | **After Sorting**            |
|---------------------------------|------------------------------|------------------------------|
| Empty array                     | `[]`                         | `[]`                         |
| Already sorted array            | `[1, 2, 3, 4, 5]`            | `[1, 2, 3, 4, 5]`            |
| Reverse-sorted array            | `[5, 4, 3, 2, 1]`            | `[1, 2, 3, 4, 5]`            |
| Array with repeated elements    | `[2, 2, 2, 2, 2]`            | `[2, 2, 2, 2, 2]`            |
| Random array                    | `[12, 3, 5, 7, 19, 4]`       | `[3, 4, 5, 7, 12, 19]`       |

## Links to Other Files


- [Hash Table Implementation](./hash_table_chaining.py)


## 1. Key Idea of Randomized Quicksort
Randomized Quicksort works similarly to standard Quicksort but selects the pivot randomly. This random selection ensures that, on average, the partitioning process is balanced, preventing the worst-case (O(n^2)) behavior. As described in the book, *if, at each level of recursion, the partitioning procedure places a constant fraction of the elements on either side of the pivot, the recursion tree has a depth of Θ(log n), and the work done at each level is (O(n))* (Cormen et al., 2022, p. 194). This results in an expected running time of (O(n log n)).

## 2. Indicator Random Variables for Comparisons
We use **indicator random variables** to analyze the expected number of comparisons made during partitioning.

### 2.1 Indicator Variable Definition
Let $X_{ij}$ be an indicator random variable where:

$$
X_{ij} =
\\begin{cases} 
1 & \\text{if elements } i \\text{ and } j \\text{ are compared during the execution}, \\\\
0 & \\text{otherwise}.
\\end{cases}
$$

### 2.2 Expected Comparisons
According to Theorem 7.4 in the book, the total number of comparisons performed in Randomized Quicksort can be expressed as:

$$
E[X] = \\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n} E[X_{ij}] = \\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n} \\frac{2}{j - i + 1}
$$

By summing this over all element pairs, we get:

$$
E[X] = O(n \\log n)
$$

This result shows that the expected number of comparisons—and thus the running time—is $O(n \\log n)$ (Cormen et al., 2022, p. 197).

### Conclusion
As outlined in the book, the expected running time of Randomized Quicksort is $O(n \\log n)$ because the recursion tree has a depth of $\\log n$ and each level performs $O(n)$ comparisons. The use of indicator random variables confirms that the expected number of comparisons is $O(n \\log n)$, ensuring that Randomized Quicksort is efficient for average-case performance (Cormen et al., 2022, p. 198).

### 3. Comparison: Randomized Quicksort vs Deterministic Quicksort
 This is an analysis of **Randomized Quicksort** and **Deterministic Quicksort** (first element as the pivot), focusing on both theoretical time complexity and empirical performance under various input conditions. The algorithms were tested on random arrays, sorted arrays, reverse-sorted arrays, and arrays with repeated elements.

### Theoretical Analysis:

### 3.1 Randomized Quicksort

- **Time Complexity**: The expected time complexity of Randomized Quicksort is $O(n \log n)$, due to the random pivot selection leading to balanced partitions on average. Using the Master Theorem for divide-and-conquer algorithms, the recurrence relation is:

$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
$$

which resolves to $O(n \log n)$ (Cormen et al., 2022, p. 197).

- **Advantages**: Random pivot selection helps avoid the worst-case behavior, even for sorted or reverse-sorted arrays. This randomization ensures efficient performance across various input types.

## 3.2 Deterministic Quicksort (First Element as Pivot)

- **Time Complexity**: In the average case, the time complexity of Deterministic Quicksort is $O(n \log n)$, similar to Randomized Quicksort. However, when the input is already sorted or reverse-sorted, the worst-case time complexity degrades to $O(n^2)$, due to highly unbalanced partitions caused by the first element being used as the pivot.

$$
T(n) = T(n-1) + O(n)
$$

- **Disadvantages**: Deterministic Quicksort suffers significantly when sorting already sorted or reverse-sorted arrays due to poor pivot choices, which leads to $O(n^2)$ behavior (Cormen et al., 2022, p. 198).

### Empirical Comparisons:

### Experimental Setup

The algorithms were tested on the following input distributions for array sizes of 100, 1000, 5000, and 10000 elements:
- **Random arrays**
- **Already sorted arrays**
- **Reverse-sorted arrays**
- **Arrays with repeated elements**

Both **Randomized Quicksort** and **Deterministic Quicksort** were implemented iteratively to avoid recursion depth limits.

### Results Overview

| Input Size | Array Type        | Randomized Quicksort (Seconds) | Deterministic Quicksort (Seconds) |
|------------|-------------------|-------------------------------|-----------------------------------|
| 100        | Random            | 0.000163                      | 0.000101                          |
| 100        | Sorted            | 0.000152                      | 0.000245                          |
| 100        | Reverse-Sorted    | 0.000147                      | 0.000416                          |
| 100        | Repeated Elements | 0.000230                      | 0.000213                          |
| 1000       | Random            | 0.002043                      | 0.001524                          |
| 1000       | Sorted            | 0.002176                      | 0.024659                          |
| 1000       | Reverse-Sorted    | 0.002024                      | 0.042171                          |
| 1000       | Repeated Elements | 0.009319                      | 0.008433                          |
| 5000       | Random            | 0.011467                      | 0.008750                          |
| 5000       | Sorted            | 0.011896                      | 0.596874                          |
| 5000       | Reverse-Sorted    | 0.011495                      | 0.906454                          |
| 5000       | Repeated Elements | 0.203166                      | 0.200576                          |
| 10000      | Random            | 0.023788                      | 0.020315                          |
| 10000      | Sorted            | 0.025155                      | 2.496401                          |
| 10000      | Reverse-Sorted    | 0.024351                      | 3.273677                          |
| 10000      | Repeated Elements | 0.797911                      | 0.773329                          |

## Discussion of Results

### **Randomized Quicksort**:
- **Random Arrays**: Performed consistently well across all input sizes, confirming the expected $O(n \log n)$ time complexity.
- **Sorted and Reverse-Sorted Arrays**: Randomized Quicksort maintained stable performance, as random pivot selection avoids unbalanced partitions, even in sorted and reverse-sorted arrays.
- **Repeated Elements**: Performance was slightly worse than random arrays due to the presence of identical elements, which can reduce the effectiveness of partitioning.

### **Deterministic Quicksort**:
- **Random Arrays**: Performed similarly to Randomized Quicksort on random inputs, confirming the expected $O(n \log n)$ behavior.
- **Sorted and Reverse-Sorted Arrays**: As expected, performance degraded drastically on these inputs, demonstrating the worst-case $O(n^2)$ behavior due to poor pivot selection (first element).
- **Repeated Elements**: Showed relatively stable performance, though slightly worse than random arrays.

## Conclusion

The empirical results align with the theoretical analysis. **Randomized Quicksort** performed consistently across all input types, while **Deterministic Quicksort** showed significant performance degradation for sorted and reverse-sorted arrays. Randomized Quicksort is a more reliable algorithm for handling diverse input types due to its resilience against worst-case behavior.


## References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
- Wikibooks. (2023). LaTeX/Mathematics. Retrieved from https://en.wikibooks.org/wiki/LaTeX/Mathematics
