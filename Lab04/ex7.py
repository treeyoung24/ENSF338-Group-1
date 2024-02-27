def reverse(self):
    if not self.head:
        return
    
    prev_node = None
    curr_node = self.head
    
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    
    self.head = prev_node
