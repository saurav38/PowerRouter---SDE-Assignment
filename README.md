# PowerRouter---SDE-Assignment
<p> 1. In this solution, we first define the old queue and the current index value. We also define the list of inactive members, which in this case is ['A', 'D']. Then, we remove the inactive members from the old queue to obtain the new queue.

Next, we find the Current Index Member in the old queue by indexing it with the current index value. If the Current Index Member is inactive, we find the next available member by iterating over the remaining members in the old queue and checking if they are inactive. If we reach the end of the queue without finding an active member, we wrap around to the beginning of the queue.

Finally, we find the index of the Current Index Member in the new queue using the index() method and print the results.</p>
<br>
<p> 3.  we are using two pointers: slow_ptr and fast_ptr. The slow_ptr moves one node at a time, while the fast_ptr moves two nodes at a time. By the time the fast_ptr reaches the end of the linked list, the slow_ptr will be pointing to the middle node of the linked list. If the number of nodes in the linked list is even, then the function returns the data at the second middle node.
</p>

