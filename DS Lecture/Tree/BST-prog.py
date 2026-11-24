#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        #self.cnt=0   Total nodes counter
        self.lcnt=0
        self.nlcnt=0
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None:
                self.lcnt+=1
            if rt.left is not None or rt.right is not None:
                self.nlcnt+=1
            #self.cnt+=1    Total nodes
            self.inorder(rt.right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def findminmax(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\nMin Value:",temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\n Max Value:",temp.data)

    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))
print("\nInorder: ")
b1.inorder(b1.root)
#print("\n Total nodes:",b1.cnt)
print("\n Total no of leaf nodes:",b1.lcnt)
print("\n Total no of non leaf nodes:",b1.nlcnt)
print("\nPreorder: ")
b1.preorder(b1.root)
print("\nPostorder: ")
b1.postorder(b1.root)
b1.findminmax(b1.root)