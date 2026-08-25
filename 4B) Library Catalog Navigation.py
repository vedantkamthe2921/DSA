class CategoryNode:
    def __init__(self, name):
        self.name = name
        self.left = None   # Subcategory / Specific topic (Left branch)
        self.right = None  # Subcategory / Specific topic (Right branch)


def build_catalog():
    name = input("Enter Category/Section name (type 'done' for empty/leaf): ").strip()
    if name.lower() == "done" or not name:
        return None

    node = CategoryNode(name)
    print(f"Enter left subcategory/sub-genre under '{name}':")
    node.left = build_catalog()
    print(f"Enter right subcategory/sub-genre under '{name}':")
    node.right = build_catalog()
    return node


# Hierarchical Tree Display (Top-Down Catalog Map)
def display_tree(root, indent="", is_left=True):
    if root is not None:
        print(indent + ("|-- Left: " if is_left else "`-- Right: ") + root.name)
        display_tree(root.left, indent + ("|   " if is_left else "    "), True)
        display_tree(root.right, indent + ("|   " if is_left else "    "), False)


# Interactive Catalog Navigation (Drill-down browsing)
def browse_catalog(root):
    if root is None:
        print("The library catalog is currently empty.")
        return

    curr = root
    while curr:
        print(f"\n[Current Section]: {curr.name}")
        
        # Check if it is a terminal/leaf shelf
        if curr.left is None and curr.right is None:
            print(">> You have reached the final shelf for this section.")
            break

        print("Navigation Options:")
        if curr.left:
            print(f"  1. Go to Left Subsection: '{curr.left.name}'")
        if curr.right:
            print(f"  2. Go to Right Subsection: '{curr.right.name}'")
        print("  3. Stop Browsing")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1' and curr.left:
            curr = curr.left
        elif choice == '2' and curr.right:
            curr = curr.right
        elif choice == '3':
            print("Exiting navigation.")
            break
        else:
            print("Invalid direction or empty shelf. Try again.")


def main():
    print("=== Library Catalog Tree Setup ===")
    root = build_catalog()

    while True:
        print("\n=== Library Catalog Navigation Menu ===")
        print("1. Display Full Category Hierarchy")
        print("2. Browse / Navigate Down Shelves")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            print("\n--- Library Hierarchy Tree ---")
            if root:
                print(f"[Root Section]: {root.name}")
                display_tree(root.left, " ", True)
                display_tree(root.right, " ", False)
            else:
                print("Catalog is empty.")
            print("------------------------------")
        elif choice == '2':
            browse_catalog(root)
        elif choice == '3':
            print("Thank you for using the Library Catalog Navigation System!")
            break
        else:
            print("Invalid choice! Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
  
