class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        temp = Node(data)
        temp.next = self.first
        self.first = temp

    def removeFirst(self):
        if self.first is None:
            print("List is empty")
        else:
            cur = self.first
            self.first = self.first.next
            print("The deleted item is", cur.data)

    def display(self):
        if self.first is None:
            print("List is empty")
            return
        cur = self.first
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()  # Add a newline for better formatting

    def search(self, item):
        if self.first is None:
            print("List is empty")
            return

        cur = self.first
        while cur:
            if cur.data == item:
                print("Item is Present in the Linked list")
                return
            cur = cur.next  # Move to the next node *inside* the loop

        print("Item is not present in the Linked list")  # Print this *after* the loop


# Singly Linked List
sll = SinglyLinkedList()
while True:
    try:  # Handle potential errors like invalid input
        ch = int(input("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit :"))
        if ch == 1:
            item = input("Enter the element to insert:")
            sll.insertFirst(item)
            sll.display()
        elif ch == 2:
            sll.removeFirst()
            sll.display()
        elif ch == 3:
            item = input("Enter the element to search:")
            sll.search(item)
        elif ch == 4:
            sll.display()
        elif ch == 5:
            break
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")