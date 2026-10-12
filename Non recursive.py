class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter the data (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of {x}")
    root.left = create()

    print(f"Enter right of {x}")
    root.right = create()

    return root


class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return None

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


def preorder(root):
    s = Stack()

    while root is not None or s.TOP != -1:

        while root is not None:
            print(root.data)
            s.push(root)
            root = root.left

        root = s.pop()

        if root is not None:
            root = root.right


def inorder(root):
    s1 = Stack()

    while root is not None or s1.TOP != -1:

        while root is not None:
            s1.push(root)
            root = root.left

        root = s1.pop()

        if root is not None:
            print(root.data)
            root = root.right
