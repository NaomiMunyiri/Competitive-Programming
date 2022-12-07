class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=ListNode() #object listNode:result will be linkedlist
        current=x #points at position of inserting new node

        carry=0
        while l1 or l2: #while they have digits
            v1=l1.val if l1 else 0 #digit of l1 if l1 is not null
            v2=l2.val if l2 else 0

            val = v1 + v2 + carry
            carry=val // 10 #if val > 10, need to remove carry ie 15 rm 5
            val= val % 10 #if val > 10, get ones place ie 15 rm 5
            current.next=ListNode(val) #insert into list

            current=current.next #update pointer
            l1=l1.next if l1 else None #..... if non null
            l2=l2.next if l2 else None #.................
        return x.next 