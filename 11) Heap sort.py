#Implement Heap sort to sort given numbers using Min Heap (Descending)/Max Heap (Ascending).
def heapify(arr, n, root, heap_type):
    """
    Restore the heap property in the subtree rooted at root.
    heap_type = 'max' for Max Heap, 'min' for Min Heap.
    """
    selected = root
    left = 2 * root + 1
    right = 2 * root + 2
 
    if heap_type == "max":
        if left < n and arr[left] > arr[selected]:
            selected = left
        if right < n and arr[right] > arr[selected]:
            selected = right
    else:
        if left < n and arr[left] < arr[selected]:
            selected = left
        if right < n and arr[right] < arr[selected]:
            selected = right
 
    if selected != root:
        arr[root], arr[selected] = arr[selected], arr[root]
        heapify(arr, n, selected, heap_type)
 
 
def heap_sort(numbers, heap_type):
    arr = numbers.copy()
    n = len(arr)
 
    # Build the selected heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)
 
    # Move the root to the end and restore the heap.
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0, heap_type)
 
    return arr
 
 
def main():
    n = int(input("Enter number of elements: "))
 
    if n < 0:
        print("Number of elements cannot be negative.")
        return
 
    numbers = []
    for i in range(n):
        value = int(input("Enter element: "))
        numbers.append(value)
 
    print("\\n1. Min Heap - Descending Order")
    print("2. Max Heap - Ascending Order")
    choice = int(input("Enter your choice: "))
 
    print("\\nOriginal list:", numbers)
 
    if choice == 1:
        result = heap_sort(numbers, "min")
        print("Sorted list (Descending using Min Heap):", result)
    elif choice == 2:
        result = heap_sort(numbers, "max")
        print("Sorted list (Ascending using Max Heap):", result)
    else:
        print("Invalid choice. Please select 1 or 2.")
 
 
if __name__ == "__main__":
    main()
