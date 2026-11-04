#Linear queue using linkedlist
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LQueue:
    def __init__(self):
        self.front=self.rear=None

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
        print("deleted Node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Queue is empty")
            self.rear=None
        temp=None

    # 3. Display
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    # 4. Reverse Queue using Stack
    def reverse(self):
        stack = []
        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(Node(stack.pop()))

    # 5. Merge two Queues into one
    def merge(self, q2):
        q3 = LQueue()

        temp = self.front

        while temp:
            q3.enqueue(Node(temp.data))
            temp = temp.next

        temp = q2.front

        while temp:
            q3.enqueue(Node(temp.data))
            temp = temp.next

        return q3

    # 6. Check whether two Queues are Identical
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None

    
que=LQueue()
que.enqueue(Node(23))
que.enqueue(Node(40))
que.enqueue(Node(20))
que.enqueue(Node(38))
print("First Queue:")
que.print()
print("\nAfter Dequeue:")
que.dequeue()

# Reverse Queue
print("\nReversed Queue:")
que.reverse()
que.print()

# Second Queue
que2 = LQueue()

que2.enqueue(Node(10))
que2.enqueue(Node(20))
que2.enqueue(Node(30))

print("\nSecond Queue:")
que2.print()

# Merge two Queues
print("\nMerged Queue:")
que3 = que.merge(que2)
que3.print()

# Check Identical Queues
print("\nCheck Identical:")

if que.identical(que2):
    print("Both Queues are Identical")
else:
    print("Both Queues are Not Identical")