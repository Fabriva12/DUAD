class Node:
    data = str
    next = "Node"
    def __init__(self, data,):
        self.data = data
        self.next = None

class Double_Ended:
    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def push_right(self, new_node):
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop_left(self):
        self.head = self.head.next

    def pop_right(self):
        current_node = self.head
        next_node = current_node.next
        while (next_node is not None):
            current_node = next_node
            next_node = current_node.next
        current_node.next = None

dll = Double_Ended()

dll.push_left(Node("helloooooo"))
dll.push_left(Node("I'm the first"))
dll.push_left(Node("hi"))
dll.pop_left()
dll.print_structure()