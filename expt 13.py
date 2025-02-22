class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.first = None

    # Function to insert a node at the end of the list
    def insertAtEnd(self, data):
        temp = Node (data)
        if self.first is None:  # If the list is empty
            self.first = temp
        else:
            cur = self.first  # Start from the first element
            while cur.next != None:  # Traverse until it reaches the last node
                cur = cur.next
            cur.next = temp
            temp.prev = cur

    def deleteFirst(self):
        if self.first is None:
            print ("list is empty")
        elif self.first.next is None:
            print ("the deleted item is", self.first.data)
            self.first = None  # Remove the last node, which was the first one
        else:
            cur = self.first
            self.first = self.first.next  # Replace the head with the new first node
            self.first.prev = None  # Update previous nodes of the deleted ones
            print ("the deleted item is", cur.data)

    def search(self, data):
        if self.first is None:
            print ("list is empty")
            return False
        else:
            cur = self.first
            while cur != None:
                if cur.data == data:
                    print ("Item is present in the Linked list")
                    return True
                else:
                    cur = cur.next
                print ("Item is not present in the Linked list")

    def display(self):
        if self.first == None:
            print ("list is empty")
        else:
            cur = self.first
            while cur != None:
                print (cur.data, end=" ")
                cur = cur.next


dll = DoublyLinkedList ( )
while True:  # Continue until the user chooses to exit
    ch = int (input ("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit :"))
    if (ch == 1):
        item = input ("Enter the element to insert:")
        dll.insertAtEnd (item)
        print (f"Successfully inserted at the end of the list: {item}")
    elif (ch == 2):
        dll.deleteFirst ( )
        print (f"Successfully deleted first node.")
    elif (ch == 3):
        data = input ("Enter the element to search:")
        if dll.search (data):
            print ("Element is present in the Linked List")
        else:
            print ("Element is not present in the Linked List")
    elif ch == 4:
        dll.display ( )
    elif (ch == 5):
        break
    else:
        print ("Invalid choice, try again.")
