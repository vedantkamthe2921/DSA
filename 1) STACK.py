class LibraryBookStack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, book_title):
        if self.is_full():
            print("Error: Stack Overflow! Return counter is full.")
            return
        self.stack.append(book_title)
        print(f"Book '{book_title}' added to the return stack.")

    def pop(self):
        if self.is_empty():
            print("Error: Stack Underflow! No returned books to process.")
            return None
        removed_book = self.stack.pop()
        print(f"Processing and shelving: '{removed_book}'")
        return removed_book

    def peek(self):
        if self.is_empty():
            print("No books currently in the return stack.")
            return None
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("The return stack is empty.")
            return
        print("\n--- Current Returned Books Stack (Top to Bottom) ---")
        for book in reversed(self.stack):
            print(f"| {book} |")
        print("----------------------------------------------------\n")


def main():
    library = LibraryBookStack(capacity=50)

    while True:
        print("\n=== Library Book Return Management ===")
        print("1. Return a Book (Push)")
        print("2. Process/Shelve a Book (Pop)")
        print("3. View Top Book (Peek)")
        print("4. Display All Returned Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter the book title to return: ").strip()
            if title:
                library.push(title)
            else:
                print("Book title cannot be empty.")
        elif choice == '2':
            library.pop()
        elif choice == '3':
            top_book = library.peek()
            if top_book:
                print(f"Next book to be shelved: '{top_book}'")
        elif choice == '4':
            library.display()
        elif choice == '5':
            print("Exiting Library Book Return System. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
