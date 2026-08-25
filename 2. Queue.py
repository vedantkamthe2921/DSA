class TicketCounterQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.size - 1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, customer_name):
        if self.is_full():
            print("Queue Overflow! The booking counter line is full.")
            return

        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = customer_name
        print(f"Customer '{customer_name}' joined the queue at position {self.rear + 1}.")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No customers waiting in the line.")
            return None

        customer = self.queue[self.front]
        print(f"Ticket booked! Served customer: '{customer}'")
        self.front += 1

        # Reset pointers when queue becomes completely empty
        if self.front > self.rear:
            self.front = -1
            self.rear = -1

        return customer

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No customer at the counter.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("The booking counter queue is empty.")
            return

        print("\n--- Current Ticket Counter Queue (Front to Rear) ---")
        for i in range(self.front, self.rear + 1):
            print(f"[{i - self.front + 1}] {self.queue[i]}")
        print("---------------------------------------------------\n")


def main():
    counter = TicketCounterQueue(size=5)

    while True:
        print("\n=== Ticket Booking Counter ===")
        print("1. Add Customer to Line (Enqueue)")
        print("2. Issue Ticket to Customer (Dequeue)")
        print("3. View Next Customer (Peek)")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter customer name: ").strip()
            if name:
                counter.enqueue(name)
            else:
                print("Name cannot be empty.")
        elif choice == '2':
            counter.dequeue()
        elif choice == '3':
            next_person = counter.peek()
            if next_person:
                print(f"Next customer to be served: '{next_person}'")
        elif choice == '4':
            counter.display()
        elif choice == '5':
            print("Closing the ticket booking counter. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
