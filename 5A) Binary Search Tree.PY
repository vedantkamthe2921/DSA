class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, n):
    if root is None:
        return Node(n)
    if root.data < n:
        root.right = insert(root.right, n)
    else:
        root.left = insert(root.left, n)
    return root

def create():
    root = None
    while True:
        x = int(input("Enter data to create node (0 to stop): "))
        if x == 0:
            break
        root = insert(root, x)
    return root

class stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("stack overflow")
            return
        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack underflow")
            return
        x = self.st[self.TOP]
        self.TOP -= 1
        return x

def preorder(root):
    if root is None:
        return
    s = stack()
    print("preorder traversal is =")
    s.push(root)
    while s.TOP != -1:
        curr = s.pop()
        print(curr.data)
        if curr.right is not None:
            s.push(curr.right)
        if curr.left is not None:
            s.push(curr.left)

def inorder(root):
    if root is None:
        return
    s = stack()
    curr = root
    print("inorder traversal is =")
    while curr is not None or s.TOP != -1:
        while curr is not None:
            s.push(curr)
            curr = curr.left
        curr = s.pop()
        print(curr.data)
        curr = curr.right

def postorder(root):
    if root is None:
        return
    s1 = stack()
    s2 = stack()
    print("postorder traversal is =")
    s1.push(root)
    while s1.TOP != -1:
        curr = s1.pop()
        s2.push(curr)
        if curr.left is not None:
            s1.push(curr.left)
        if curr.right is not None:
            s1.push(curr.right)
    while s2.TOP != -1:
        curr = s2.pop()
        print(curr.data)

root = create()
preorder(root)
inorder(root)
postorder(root)
