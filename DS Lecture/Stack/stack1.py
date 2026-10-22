#Stack implementation using linkelist 
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None
    
    def push(self,newnode):
        newnode.next=self.top
        self.top=newnode

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            print("Poped Element",temp.data)
            self.top=self.top.next
            temp=None

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("stack contains ...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next

    #Reverse Stack Using another stack
    def reverse(self):
        temp=self.top
        while temp:
            st1.push(Node(temp.data))
            temp=temp.next
        

st=Stack()
st1=Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()
st.pop()
st.print()
st.reverse()
st1.print()