class Node:#represents individual members in linked list..two classmembers:data and next
    def __init__(self, data=None, next=None):
        self.data=data #data
        self.next=next #pointer to next element

class LinkedList:
    def __init__(self):
        self.head=None #points to head of linked list

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+= str(itr.data) + '-->'
            itr=itr.next #iterates through element one by one

        print(llstr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data,None)

    def insert_values(self,data_list):#takes list of values and creates linked list
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    
    def get_length(self):#returns length of linked list
        count = 0
        itr= self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self,index):#removes element at given index
        if index<0 or index>+self.get_length():
            raise Exception("Invalid")
        
        if index==0:#if removing head
            self.head=self.head.next#point to next element
            return
        
        count=0
        itr=self.head
        while itr:
            if count == index-1:#you stop at the previous element link
                itr.next=itr.next.next
                break

            itr=itr.next
            count+=1

    def insert_at(self,index,data):#inserts at specific index
        if index<0 or index>+self.get_length():
            raise Exception("Invalid")
        
        if index==0:
            self.insert_at_beginning(data)
            return
            
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=Node
                break
            itr=itr.next                
            count+=1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return

        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.data.next=Node(data_to_insert,itr.data.next)
                break
            itr.itr.next
    
    def remove_by_value(self,data):
        if self.head is None:
            return
        
        if self.head.data==data:
            self.head=self.head.next
        
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next.data=itr.next.next
                break
            itr.itr.next

    


if __name__=='__main__':
    ll = LinkedList()
   # ll.insert_at_beginning(5)
    #ll.insert_at_beginning(89)
    #ll.insert_at_end(79)
    #ll.insert_at_end(15)
    #ll.insert_values(["banana","mango","oranges"])
    #ll.remove_at(2)
    #ll.remove_at(20)
    #print(ll.get_length())
    #ll.insert_at(0,"figs")
    ll.insert_at(0,"apple")
    ll.print()
 