class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.first = None

    def insertAtEnd(self, data):
        temp = Node (data)

        if not self.first:
            self.first = temp
        else:
            cur = self.first
            while True:
                cur = cur.next
                if cur == self.first:  # Check for the end of the list
                    break
                cur.next = temp  # Insert at the end

    def deleteAtEnd(self):
        if not self.first or not self.first.next:
            print ("The circular linked list is empty")
            return

        cur = self.first
        while True:
            cur = cur.next
            if cur == self.first:
                break

        pr = cur  # Point to the previous node
        temp = cur.next  # Point to the end of the current range
        cur.next = temp
        temp.next = self.first

        if not self.first:
            self.first = None
        else:
            while cur.next != self.first:
                cur = cur.next

        del pr

    def display(self):
        if not self.first:
            print ("The circular linked list is empty")
            return

        cur = self.first
        while True:
            print (cur.data, end=" ")
            cur = cur.next
            if cur == self.first:
                break

        print ( )


def search(self, item):
    if not self.first:
        print ("The circular linked list is empty")
        return False
    cur = self.first
    while True:
        if cur.data == item:
            return True
        else:
            cur = cur.next


# Example usage:
cll = CircularLinkedList ( )
while (True):
    ch = int (input ("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit :"))
    if (ch == 1):
        data = input ("Enter the element to insert:")
        cll.insertAtEnd (data)
        print (f"Element '{data}' has been inserted at the end.")

    elif (ch == 2):
        cll.deleteAtEnd ( )
        print ("\nDelete operation completed.\n")

    elif (ch == 3):
        data = input ("Enter the element to search:")
        if cll.search (data):
            print (f"The element '{data}' has been found in the list.")
        else:
            print (f"The element '{data}' is not present in the list.")

    elif (ch == 4):
        cll.display ( )

    elif (ch == 5):
        break

