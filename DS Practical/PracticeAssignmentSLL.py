class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head

            while temp.next:
                temp=temp.next
            temp.next=new_node

    def insert(self,new_node,pos):
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            count=1
            temp=self.head
            while count< pos-1:
                temp=temp.next
                count+=1

            new_node.next=temp.next
            temp.next=new_node


    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)
        else:
            print("Linked list is empty")


    def del_node(self,value):
        temp=self.head
        if temp.data==value:
            self.head=self.head.next
            return 
        while(temp):
            if temp.data==value:
                break
            else:
                prev=temp
                temp=temp.next

        if temp==None:
            print("Value is not present")
            return
        prev.next=temp.next
        temp=None

    def reverse(self):
        print("Reverse List:")
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev

    def sum_pairs(self):
        print("Sum of pairs:")
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(total)
            temp = temp.next.next


    def print(self):
        temp=self.head

        while(temp):
            print(temp.data)
            temp=temp.next

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(40)

list.append(n1)
list.append(n2)
list.append(n3)
list.insert(Node(30),3)
list.insert(Node(50),5)
list.print()
list.middle()
list.del_node(20)
list.reverse()
list.print()
list.sum_pairs()
list.print()

