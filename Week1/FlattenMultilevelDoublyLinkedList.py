"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    #O(n)
    #use stack
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy=Node(0) #track head
        current,stack=dummy,[head]
        while stack:
            tmp=stack.pop()
            if tmp.next: #if has next
                stack.append(tmp.next)
            if tmp.child: #if has child
                stack.append(tmp.child)
            current.next=tmp #that was popped
            tmp.previous=current #prev point to current
            tmp.child=None
            current=tmp #moves pointer
        dummy.next.prev=None
        return dummy.next