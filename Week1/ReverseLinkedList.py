#iterattive-O(n)
#pp cp   tmp
#    1 -> 2  -> 3 -> None
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None #pointer
        cur=head #pointer

        while cur:
            tmp=cur.next 
            cur.next=prev #current to prev
            prev=cur #pre to cur
            cur=tmp #cur to tmp
            #till cp is None
        return prev

#recursive-return tail node
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev,cur):
            if not cur:
                return prev
            tail=rec(cur,cur.next)
            cur.next=prev

            return tail
        return rec(None,head)