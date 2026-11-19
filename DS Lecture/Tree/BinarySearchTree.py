#binary search tree
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,new_node):
        if self.root is None:#Creating the root node
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                elif new_node.data>=temp.data:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def inorder(self,temp):#recursive
        if temp is None:#terminating condition
            return
        else:
            self.inorder(temp.left)#recursive call
            print(temp.data,end=" ")
            self.inorder(temp.right)#recursive call

btree=BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))

btree.inorder(btree.root)

    



        

