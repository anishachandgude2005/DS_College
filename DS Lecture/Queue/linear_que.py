#Linear queue using linkedlist
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,newnode):
        if self.rear:
            self.rear.next=newnode
            self.rear=newnode
        else:
            self.front=self.rear=newnode
    def dequeue(self):
        temp=self.front
        print("deleted Node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Queue is empty")
            self.rear=None
        temp=None

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
que=LQueue()
que.enqueue(Node(23))
que.enqueue(Node(40))
que.enqueue(Node(20))
que.enqueue(Node(38))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()