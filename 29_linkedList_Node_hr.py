class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):

        newNode = Node(data)

        # Case 1: Empty list
        if head is None:
            return newNode

        # Case 2: Traverse to the last node
        current = head
        while current.next is not None:
            current = current.next

        # Insert new node at tail
        current.next = newNode

        return head




    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  