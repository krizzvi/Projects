class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        current = self.head
        print("Linked List: [ ", end="")
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print("]")
        print(f'head = {self.head.value} tail = {self.tail.value} size = {self.size}')

    def addFirst(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def add(self, k, value): # add the node at index k
        if k < 0 or k > self.size:
            raise IndexError('Index out of bounds!')

        if k == 0:
            self.addFirst(value)
            return
        node = Node(value)
        current = self.head
        i = 0

        #Traverse to the (k-1)th node
        while i < k-1:
            current = current.next
            i += 1

        # insert the new node after (k-1)th node
        node.next = current.next
        current.next = node

        if current == self.tail:
            self.tail = node
        self.size += 1

    def delete(self, k):  # delete the node at index k
        if k < 0 or k >= self.size:
            raise IndexError('Index out of bounds!')

        if k == 0:  # Deleting the head node
            self.head = self.head.next
            if self.size == 1:  # If it was the only node, update the tail
                self.tail = None
        else:
            current = self.head
            i = 0

            # Traverse to the (k-1)th node
            while i < k - 1:
                current = current.next
                i += 1

            # Remove the k-th node
            to_delete = current.next
            current.next = to_delete.next

            # Update tail if we are deleting the last node
            if to_delete == self.tail:
                self.tail = current
        self.size -= 1

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # After reversal, the head will become the tail

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  # Set the new head of the list

# Driver code
ll = LinkedList()
# add 10 nodes to the linked list
for i in range(10):
    print(f'>>> Inserting {i*i} as node #{i}')
    ll.add(i, i*i)
    ll.print_list()

# insert a new node with value '100' as the head
print(f'>>> Inserting {100} as node #{1}')
ll.add(0, 100)
ll.print_list()

# Delete nodes
print(f'>>> Deleting node #{1}')
ll.delete(0)
ll.print_list()

print(f'>>> Deleting node #{5}')
ll.delete(4)
ll.print_list()

# Reverse the list
print('>>> Reversing the list')
ll.reverse()
ll.print_list()
