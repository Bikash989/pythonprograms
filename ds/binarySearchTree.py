class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def insert(root,node):
    if root is None:
        root = node
    else:
        if node.val > root.val:
            if root.right is None:
                root.right = node
            else:
                return insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                return insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)


root = Node(15)
insert(root,(Node(50)))
insert(root,Node(20))
insert(root,Node(234))
insert(root,Node(12))

inorder(root)
print()