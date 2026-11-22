from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                print(f"Duplicate value {data} ignored.")
                return

    def level_order(self):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = deque([self.root])
        level = 0

        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end="")

            for _ in range(level_size):
                node = queue.popleft()
                print(node.data, end=" ")

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            print()
            level += 1

    def height(self, node):
        # Height is measured in edges.
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def print_leaf_nodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=" ")
            return

        self.print_leaf_nodes(node.left)
        self.print_leaf_nodes(node.right)


def main():
    original_tree = BinarySearchTree()
    new_tree = BinarySearchTree()

    n = int(input("Enter number of nodes: "))
    if n < 0:
        print("Number of nodes cannot be negative.")
        return

    values = []
    for i in range(n):
        value = int(input(f"Enter value {i + 1}: "))
        values.append(value)
        original_tree.insert(value)

    # Build a separate BST using the same input sequence.
    for value in values:
        new_tree.insert(value)

    print("\nOriginal BST - Level-wise:")
    original_tree.level_order()

    print("\nNew BST - Level-wise:")
    new_tree.level_order()

    print("\nHeight of Original BST (in edges):",
          original_tree.height(original_tree.root))

    print("Leaf Nodes of Original BST: ", end="")
    original_tree.print_leaf_nodes(original_tree.root)
    print()


if __name__ == "__main__":
    main()
