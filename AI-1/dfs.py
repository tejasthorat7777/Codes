class Node:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data)
        InOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal of binary tree is : ")
InOrder(root)