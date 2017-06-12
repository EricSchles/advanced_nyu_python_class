# psuedo code version
# record DoublyLinkedNode {
#     prev // A reference to the previous node
#     next // A reference to the next node
#     data // Data or a reference to data
# }
# code for this psuedo code below


class DoublyLinkedNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return repr(self.data)

# record DoublyLinkedList {
#      DoublyLinkedNode firstNode   // points to first node of list
#      DoublyLinkedNode lastNode    // points to last node of list
# }
# code for this psuedo code below


class DoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def traverse_forward(self):
        node = self.first_node
        while node is not None:
            print(node.data)
            node = node.next

    def traverse_backward(self):
        node = self.last_node
        while node is not None:
            print(node.data)
            node = node.prev

    def insert_after(self, node, new_node):
        new_node.prev = node
        if node.next is None:
            new_node.next = None
            self.last_node = new_node
        else:
            new_node.next = node.next
            node.next.prev = new_node
        node.next = new_node
