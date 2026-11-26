#binary search tree traverse level wise
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

    def level_order(self,rt):
        if rt is None:
            print("BST is Empty")
            return
        arr=[]
        cnt=0 # for counting visited node
        level=0
        arr.append(rt)
        while cnt<len(arr):
            node_count=len(arr)-cnt  # no of nodes to be visited
            print("\nLevel",level,":",end=" ")
            for i in range(node_count):
                temp=arr[cnt]
                cnt+=1
                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level+=1

        print("\nHeight of the tree: ",level-1)


b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))
b1.insert(Node(70))

print("\nInorder: ")
b1.inorder(b1.root)
print("\nLevel Order")
b1.level_order(b1.root)

    



        

