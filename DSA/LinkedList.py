class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def insert_at_beginning(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            current = Node(data)
            current.next = self.head
            self.head = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linkedlist = LinkedList()
# linkedlist.insert_at_end(2)
# linkedlist.insert_at_end(3)
# linkedlist.insert_at_end(4)
linkedlist.insert_at_beginning(1)
linkedlist.insert_at_beginning(2)
linkedlist.insert_at_beginning(3)
linkedlist.print_list()
