class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        """Inserts a new node at the beginning of the linked list"""
        if not self.head:
            self.head = Node(data)
            return
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def removeFirst(self):
        if self.head is None:
            print("list is empty")
        else:
            cur = self.head
            if cur.data == self.head.data:  # Check if the head needs to be removed.
                self.head = cur.next
            else:
                prev = cur
                while cur.next:
                    if cur.next.data == self.head.data:
                        break
                    prev = cur
                    cur = cur.next
                if cur.next is None:
                    del prev  # Delete the node
                else:
                    prev.next = cur.next

    def display(self):
        """Displays all the nodes of a linked list in the order they are stored"""
        if not self.head:  # Check for empty list.
            print("List is empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, end=" ")
                cur = cur.next

    def search(self, item):
        """Searches the linked list for a specific node"""
        if not self.head:  # Check for empty list.
            return False
        current = self.head
        found = False
        while current and not found:
            if current.data == item:
                found = True
            else:
                current = current.next

        return found

# Singly Linked List Example
sll = SinglyLinkedList()
while(True):
    ch = int(input("Enter your choice 1-insert 2-delete 3-search 4-display 5-exit :"))
    if (ch == 1):
        item = input("Enter the element to insert:")
        sll.insertFirst(item)
    elif (ch == 2):
        sll.removeFirst()
    elif (ch == 3):
        item = input("Enter the element to search:")
        print(sll.search(item))
    elif (ch == 4):
        sll.display()
    else:
       break
