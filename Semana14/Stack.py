class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head = None):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def push(self,data):
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self):
        self.head = self.head.next


stack= Stack()
stack.push("hi")
stack.push("hello")
stack.push("bye")
stack.pop()
stack.pop()
stack.print_structure()