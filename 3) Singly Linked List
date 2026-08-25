class BookNode:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.next = None


class LibraryCatalog:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, book_id, title, author):
        new_node = BookNode(book_id, title, author)
        new_node.next = self.head
        self.head = new_node
        print(f"Book '{title}' added at the beginning of the catalog.")

    def insert_at_end(self, book_id, title, author):
        new_node = BookNode(book_id, title, author)
        if self.head is None:
            self.head = new_node
            print(f"Book '{title}' added as the first entry.")
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        print(f"Book '{title}' added at the end of the catalog.")

    def delete_from_beginning(self):
        if self.head is None:
            print("Catalog is empty! No books to delete.")
            return None

        deleted_book = self.head
        self.head = self.head.next
        print(f"Removed '{deleted_book.title}' (ID: {deleted_book.book_id}) from the catalog.")
        return deleted_book

    def display(self):
        if self.head is None:
            print("The library catalog is empty.")
            return

        print("\n--- Dynamic Library Catalog ---")
        current = self.head
        pos = 1
        while current is not None:
            print(f"[{pos}] ID: {current.book_id} | Title: {current.title} | Author: {current.author}")
            current = current.next
            pos += 1
        print("--------------------------------\n")


def main():
    catalog = LibraryCatalog()

    while True:
        print("\n=== Library Catalog Management ===")
        print("1. Insert Book at Beginning")
        print("2. Insert Book at End")
        print("3. Delete Book from Beginning")
        print("4. Display Catalog")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice in ('1', '2'):
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            if not book_id or not title or not author:
                print("Error: All fields are required.")
                continue

            if choice == '1':
                catalog.insert_at_beginning(book_id, title, author)
            else:
                catalog.insert_at_end(book_id, title, author)

        elif choice == '3':
            catalog.delete_from_beginning()

        elif choice == '4':
            catalog.display()

        elif choice == '5':
            print("Exiting Library Catalog System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
