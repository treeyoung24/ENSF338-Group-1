Question 1.

1. Arrays

Pros: 
- Arrays allow constant-time access to elements using an index. So tasks such as accessing, updating elements will have O(1) complexity
- Tasks that require traversing the entire array or performing operations on each element have linear time complexity O(n)
- Less space required per element
Cons:
- Only works well with pre-defined size 
- Insertions or Deletions at the start will incur O(n). Very costly and inefficient for large arrays or if frequent data insertion is needed.

2. Linked Lists

Pros:
- Dynamic size, meaning it can grows or shrinks in size without having effect on performance. Therefore it's suitable for undertermined size
- Insertions or Deletions will always have time complexity of O(1)
- Only use memory proportional to the number of elements they contain which eliminates the issue of wasted memory due to unused space
Cons:
- No direct/random access to elements based on indices 
- Accessing / Updating elements require traversing the list from the beginning, which will incur O(n) time complexity
- More space is required per element. This can have a significant impact on large lists or where memory usage is a concern


Question 2.

- Use Efficient Deletion:

Implement a deletion algorithm that minimizes the number of elements that need to be shifted.
If the order of elements does not matter, we can simply overwrite the element to be deleted with the last element of the array and then reduce the array size by one. This approach avoids shifting elements and reduces the time complexity of deletion to O(1)

- Optimized Insertions:
After deletion, insert the new element directly into the position of the deleted element
If the array needs to be resized, consider resizing it to a slightly larger size to accommodate the new element without frequent resizing operations


Question 3.

1. Insertion Sort:
Insertion sort operates by iteratively inserting elements into their correct positions within the list.
In a doubly linked list, each node contains references to both its previous and next nodes, allowing for efficient traversal and insertion. Therefore, it can utilize the links between nodes to efficiently insert elements into the correct positions, maintaining the integrity of the doubly linked list structure

2. Merge Sort:
Merge sort operates by dividing the list into smaller sublists, which can be efficiently achieved in a doubly linked list by splitting the list at its midpoint. Merge sort's merging step involves merging two sorted sublists into a single sorted list and 
in a doubly linked list, merging two sorted sublists can be efficiently accomplished by rearranging the links between nodes to form a single sorted list. 

 Insertion sort can efficiently utilize the links between nodes to insert elements into their correct positions, while merge sort can leverage the divide-and-conquer approach to recursively sort and merge sublists in the doubly linked list structure. Overall both Insertion sort and Merge sort performs well on doubly linked list.


 Question 4.
 
 1. Insertion Sort:
 - Best case O(n): list is already sorted, no swaps 
 - Average Case O(n^2): randomly order list 
 - Worst Case O(n^2): list is in reverse order

In an array, insertion sort involves shifting elements to make room for the inserted element, which can be done efficiently in 
O(n) time for each insertion. However, in a doubly linked list, while traversing and finding the correct insertion position can be done in O(n) time, inserting the element requires adjusting the links between nodes, which also takes O(n) time.

2. Merge Sort:
- Best, Worst and Average Case all have time complexity of O(nlogn)

The different is that, in a normal array, merge sorts involves splitting the array into halves and merging them back together after sorting. This can be done in O(nlogn) time complexity. While in a doubly linked list, merge sort still divides the list into to halves recursively, but merging requires adjusting the links between nodes, which might incur O(n) time complexity 