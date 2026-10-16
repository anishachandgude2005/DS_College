#Singly Linear Linked List
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        temp=self.head
        if temp:
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp 
        else:#First Node
            self.head=new_node  

    def insert(self,new_node,pos):
            temp=self.head
            if pos==1:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            else:
                p=1
                while p != pos-1:
                    temp=temp.next
                    p+=1
                new_node.next=temp.next
                if temp.next:#Last position
                    temp.next.prev=new_node
                temp.next=new_node
                new_node.prev=temp

    def reverse(self):
        temp=self.head
        print("List Element:",end=" ")
        while temp :
            temp=temp.next
        while(temp):
            print(temp.data,end=" ")
            temp=temp.prev

    def print(self):
        temp=self.head
        print("List Element:",end=" ")
        while temp :
            print(temp.data,end=" ")
            temp=temp.next

list=LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.insert(Node(25),3)
list.print()
list.reverse()
list.print()