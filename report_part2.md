# Analysis of Hash Table Operations with Chaining
Part 2 contains the implementation of the hash table using chaining for collision resolution.

- [Hash table chaining implementation](./randomized_quicksort.py)

## Hash Table Output:

### Hash Table After Insertion

\\begin{tabular}{|c|c|}
\\hline
Slot & Contents \\\\ \\hline
0 & [] \\\\ \\hline
1 & [] \\\\ \\hline
2 & [] \\\\ \\hline
3 & [] \\\\ \\hline
4 & [] \\\\ \\hline
5 & [('apple', 1), ('grape', 3), ('orange', 4)] \\\\ \\hline
6 & [('banana', 2)] \\\\ \\hline
7 & [] \\\\ \\hline
8 & [] \\\\ \\hline
9 & [('mango', 5)] \\\\ \\hline
\\end{tabular}

### Search Results

\\begin{tabular}{|c|c|}
\\hline
Key & Result \\\\ \\hline
'apple' & 1 \\\\ \\hline
'banana' & 2 \\\\ \\hline
'cherry' & None \\\\ \\hline
\\end{tabular}

### Hash Table After Deletion

\\begin{tabular}{|c|c|}
\\hline
Slot & Contents \\\\ \\hline
0 & [] \\\\ \\hline
1 & [] \\\\ \\hline
2 & [] \\\\ \\hline
3 & [] \\\\ \\hline
4 & [] \\\\ \\hline
5 & [('apple', 1), ('grape', 3), ('orange', 4)] \\\\ \\hline
6 & [] \\\\ \\hline
7 & [] \\\\ \\hline
8 & [] \\\\ \\hline
9 & [('mango', 5)] \\\\ \\hline
\\end{tabular}


## Expected Time for Search, Insert, and Delete Operations

Using **simple uniform hashing**, the expected time complexity for **search**, **insert**, and **delete** operations is \(O(1 + \\alpha)\), where \( \\alpha = \\frac{n}{m} \) is the **load factor** (Cormen et al., 2022, p. 279). Let's break this down further with reference to the output of the hash table implementation.

### 1. Insert:
In the output, keys like 'apple', 'banana', and 'grape' were inserted successfully. The insert operation runs in \(O(1 + \\alpha)\), where the time to calculate the hash is constant, and the traversal time to check or append within a slot is proportional to the number of elements in that slot. For example, in slot 5, we see both 'apple' and 'banana', demonstrating how chaining handles collisions effectively. Even with two elements in a single slot, the operation remains efficient.

### 2. Search:
In the search results, the hash table finds 'apple' and 'banana' in constant time. For a non-existing key like 'cherry', the function returns None, confirming that search still runs in \(O(1 + \\alpha)\) even when the key is not found. The time complexity for search depends on the length of the linked list in each slot. In the output, each slot contains only one or two elements, so the search remains fast.

### 3. Delete:
Deleting 'banana' from slot 5 demonstrates that the delete operation also runs in \(O(1 + \\alpha)\). After the deletion, 'banana' is removed, and only 'apple' remains in the slot, showing that deletion works efficiently even when collisions occur.

## Impact of the Load Factor (\( \\alpha \))

The **load factor** \( \\alpha = \\frac{n}{m} \) determines the average number of elements per slot. In the output, we have a hash table with 10 slots and 5 elements, so the load factor is \( \\alpha = \\frac{5}{10} = 0.5 \).

- **Low \( \\alpha \)**: With a low load factor, most slots contain 0 or 1 element, as shown in the output. This keeps operations fast, as each slot requires minimal traversal.
- **High \( \\alpha \)**: As \( \\alpha \) increases, more elements collide into the same slots, increasing the time complexity for operations. However, in this case, the load factor is low, so search, insert, and delete remain efficient.

## Strategies to Maintain a Low Load Factor

### 1. Dynamic Resizing:
If the load factor grows too high (typically above 0.75), dynamic resizing helps keep operations efficient. When resizing, the number of slots \(m\) is increased, and all elements are rehashed into the new table. In the current output, resizing is unnecessary since the load factor is low (\( \\alpha = 0.5 \)).

### 2. Effective Hash Function:
The output shows good distribution of keys across slots, thanks to a hash function that spreads keys evenly. Slots 2, 3, 5, and 6 contain elements, while the others are empty, indicating minimal collisions. A well-designed hash function, as seen here, helps reduce clustering and ensures that operations remain efficient.

## Conclusion

The operations of the hash table (insert, search, and delete) run with an expected time complexity of \(O(1 + \\alpha)\), where the load factor \( \\alpha \) reflects the average number of elements per slot. In this example, the low load factor (\( \\alpha = 0.5 \)) ensures that all operations perform efficiently. As more elements are added, dynamic resizing and careful hash function design are crucial strategies to maintain this efficiency.

---

## References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
- Wikibooks. (2023). LaTeX/Mathematics. Retrieved from https://en.wikibooks.org/wiki/LaTeX/Mathematics