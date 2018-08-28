# Class to represent an individual node in the linked list
class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next_node = new_next

# Class to represent the linked list and it's operations
class LinkedList:

    def __init__(self, head=None):
        self.head = head

    # Function to insert an element to the beginning of the list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Function to obtain the size of the list
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    # Function to search for an element in the list
    def search(self, data):
        current = self.head

        while current != None:
            if current.get_data() == data:
                return current

            current = current.get_next()

        # If the element is not found in the list
        if current == None:
            return -1

    # Function to delete an element in the list
    def delete(self, data):
        current = self.head
        previous = None

        while current != None:
            if current.get_data() == data:
                # Check if the first element was deleted
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())

            else:
                previous = current
                current = current.get_next()

        # If the element is not found in the list
        if current == None:
            return -1
