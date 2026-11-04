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
            print("Poped Element",temp.data)
            self.top=self.top.next
            temp=None

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

    # 4. Reverse String using Stack
    def reverse_string(self, string):
        st = Stack()
        for ch in string:
            st.push(Node(ch))
        rev = ""
        while not st.isempty():
            rev += st.top.data
            st.pop()
        print("Reversed String:", rev)  

    # 5. Reverse Stack using another Stack
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

print("Original Stack:")
st.print()
print("\nAfter Pop:")
st.pop()
st.print()
print("\nReverse String:")
st.reverse_string("HELLO")
print("Original Stack:")
st.print()
print("Reversed Stack:")
st.reverse()
st1.print()