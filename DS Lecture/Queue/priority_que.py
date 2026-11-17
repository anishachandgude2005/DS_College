class node:
    def __init__(self,value,pr):
        self.data=value
        self.priority=pr
        self.next=None
class priorityQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.front==None: #first node to be inserted
            self.front=new_node
            return

        if self.front.priority>new_node.priority: #first position
            new_node.next=self.front
            self.front=new_node
            return
        else:
            temp=self.front
            while temp.next:
                if new_node.priority<temp.next.priority:
                    break
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
            
    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    
pq=priorityQueue()
pq.enqueue(node(100,2))
pq.enqueue(node(600,6))
pq.enqueue(node(800,12))
pq.enqueue(node(500,3))
pq.enqueue(node(300,1))
pq.display()



    
