1. The time complexity for the reverse() function is $O(n^2)$. Firstly, the outer for loop goes through every element in the list from the end, so it has complexity O(n). The self.get_element_at_pos method traverses the list to return the position of element i, so it has complexity O(n). All of the node operations have complexities O(1). So the total time complexity of the reverse() function is $O(n^2)$.
2. Avoiding use of the 'get_size()' and 'get_element_at_position(pos)' means the function will not have to traverse the list multiple times. Instead, this implementation traverses the list only once as it reverses the pointer direction of each node.



