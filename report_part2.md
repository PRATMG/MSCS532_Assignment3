# Part 2: Analysis of Hash Table Operations with Chaining
Part 2 contains the implementation of the hash table using chaining for collision resolution.


- [Here is the hash_table_chaining.py](./hash_table_chaining.py)

## The sample output has been tabulated below for clear understanding.

### Hash Table After Insertion

| Slot | Contents                               |
|------|----------------------------------------|
| 0    | []                                     |
| 1    | []                                     |
| 2    | []                                     |
| 3    | []                                     |
| 4    | []                                     |
| 5    | [('apple', 1), ('grape', 3), ('orange', 4)] |
| 6    | [('banana', 2)]                        |
| 7    | []                                     |
| 8    | []                                     |
| 9    | [('mango', 5)]                         |

### Search Results

| Key      | Result |
|----------|--------|
| 'apple'  | 1      |
| 'banana' | 2      |
| 'cherry' | None   |

### Hash Table After Deletion

| Slot | Contents                               |
|------|----------------------------------------|
| 0    | []                                     |
| 1    | []                                     |
| 2    | []                                     |
| 3    | []                                     |
| 4    | []                                     |
| 5    | [('apple', 1), ('grape', 3), ('orange', 4)] |
| 6    | []                                     |
| 7    | []                                     |
| 8    | []                                     |
| 9    | [('mango', 5)]                         |



## Analysis of Hash Table Operations with Output

Based on the output of the hash table using chaining, we observe how collisions are handled and the efficiency of the **search**, **insert**, and **delete** operations.

### Expected Time for Search, Insert, and Delete

Under **simple uniform hashing**, where keys are evenly distributed across slots, the expected time complexity for operations is $O(1 + \alpha)$, where $\alpha$ is the **load factor** ($\alpha = \frac{n}{m}$)  (Cormen et al., 2022, p. 278):

1. **Search**: In the output, searching for "apple" and "banana" was efficient, both found in the same slot. The expected search time is $O(1 + \alpha)$, where we compute the hash and traverse a short linked list, as observed with multiple elements in slot 5.

2. **Insert**: The insertion time is also $O(1 + \alpha)$. In the output, inserting "apple", "banana", and others resulted in no significant delays, even with two elements colliding into slot 5.

3. **Delete**: Deletion is performed by finding the key in the linked list and removing it. After deleting "banana", we see the remaining elements in slot 5, with the operation completed in $O(1 + \alpha)$ time.

## Impact of Load Factor ($\alpha$)

The **load factor** $\alpha = \frac{n}{m}$ impacts performance:
- **Low $\alpha$**: In the output, the load factor is $\alpha = \frac{6}{10} = 0.6$, which keeps operations efficient since most slots are either empty or contain only one or two elements.
- **High $\alpha$**: As $\alpha$ increases, more collisions occur, causing longer linked lists and slower operations, approaching $O(n)$ in the worst case.

## Strategies to Maintain Low Load Factor and Minimize Collisions

- **Dynamic Resizing**: When the load factor exceeds a certain threshold (e.g., $\alpha > 0.75$), the hash table should be resized, increasing the number of slots $m$ and rehashing all elements to maintain efficient operations.

- **Effective Hash Function**: Using a well-designed hash function, such as one from a **universal hash function family**, can help spread keys uniformly across slots, reducing the likelihood of collisions (Cormen et al., 2022, p. 277).

## Conclusion

The observed hash table operations demonstrate expected time complexities of $O(1 + \alpha)$. Keeping the load factor low through dynamic resizing and good hash function design ensures that the hash table remains efficient, even as more elements are added.

---

## References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
- Wikibooks. (2023). LaTeX/Mathematics. Retrieved from https://en.wikibooks.org/wiki/LaTeX/Mathematics
