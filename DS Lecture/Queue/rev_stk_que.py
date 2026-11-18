# Reverse stack using queue
#Reverse Queue using Stack
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    # 1. Push operation
    def push(self,newnode):
        newnode.next=self.top
        self.top=newnode

    # 2. Pop operation
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            popped_data=temp.data
            self.top=self.top.next
            temp=None
            return popped_data

    # 3. Display operation
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("stack contains ...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next


class LQueue:
    def __init__(self):
        self.front=self.rear=None

    def isempty(self):
        return self.front is None
    
    # 1. Enqueue
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next=newnode
            self.rear=newnode
        else:
            self.front=self.rear=newnode

     # 2. Dequeue
    def dequeue(self):
        temp=self.front
        dequed_data=temp.data
        self.front=self.front.next
        if self.front==None:
            print("Queue is empty")
            self.rear=None
        temp=None
        return dequed_data

    # 3. Display
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")


def reverse_stack(s1):
    q1=LQueue()
    while not s1.isempty(): # Pop from stack and enqueue to Queue
        q1.enqueue(Node(s1.pop()))    
    #q1.print()

    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()



st=Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

print("Original Stack:")
st.print()
print("Reverse Stack Using Queue:")
reverse_stack(st)
